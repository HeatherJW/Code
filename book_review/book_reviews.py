import webbrowser
import os
import re

from books import Book, Movie

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Book reviews</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #book-image {
            width: 100%;
            height: 100%;
        }
        .book-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Book reviews and movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {book_tiles}
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single book entry html template
book_tile_content = '''
<div class="col-md-6 col-lg-4 book-tile text-center">
    <img src="{book_image_url}" width="220" height="342">
    <h2>{book_title}</h2>
    <p>This book is written by {book_author}.</p>
    <p>{book_series}</p>
    <p>{book_review}</p>
</div>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

books = [
    Book('Positronic Man', 'Isaac Asimov and Robert Silverberg', None, "The Positronic Man is a 1992 novel by Isaac Asimov and Robert Silverberg, based on Asimov's novella The Bicentennial Man. It tells of a robot that begins to display characteristics, such as creativity, traditionally the province of humans; the robot is ultimately declared an official human being.", 'http://d.gr-assets.com/books/1189455449l/1867703.jpg'),
    Book('Mort', 'Terry Pratchett', 'Discworld', 'Mort is a Discworld novel by Terry Pratchett. Published in 1987, it is the fourth Discworld novel and the first to focus on the character Death, who only appeared as a side character in the previous novels. The title is the name of its main character and also a play on words: in Latin, mort means "death". The French language edition is titled Mortimer.', 'http://www.lspace.org/ftp/images/bookcovers/nl/mort-1.jpg'),
    Book('Reaper Man', 'Terry Pratchett', 'Discworld', "Reaper Man is a Discworld novel by Terry Pratchett. Published in 1991, it is the 11th Discworld novel and the second to focus on Death. The title is a reference to Alex Cox's movie Repo Man.", 'https://fanboychlop.files.wordpress.com/2012/05/reaperman.jpg'),
    Book('Hogfather', 'Terry Pratchett', 'Discworld', "Hogfather is the 20th Discworld novel by Terry Pratchett, and a 1997 British Fantasy Award nominee. The Hogfather is also a character in the book, representing something akin to Father Christmas. He grants children's wishes on Hogswatchnight (December 32) and brings them presents. He also features in other Discworld novels.", 'http://ia.media-imdb.com/images/M/MV5BODAzNzM5OTA3NF5BMl5BanBnXkFtZTcwNjMwMjE2MQ@@._V1_UY1200_CR129,0,630,1200_AL_.jpg'),
    ]

movies = [
    Movie('Hogfather', "http://ia.media-imdb.com/images/M/MV5BODAzNzM5OTA3NF5BMl5BanBnXkFtZTcwNjMwMjE2MQ@@._V1_UY1200_CR129,0,630,1200_AL_.jpg", 'https://www.youtube.com/watch?v=BaOHaBaKq-8'),
    ]

def create_book_tiles_content(books):
    content_book = ''
    for book in books:
        book_info = book.create_book_info()
        content_book += book_tile_content.format(
            book_image_url = book_info['image_url'],
            book_title = book_info['title'],
            book_author = book_info['author'],
            book_series = book_info['series'],
            book_review = book_info['review_text']
        )
    return content_book


def create_movie_tiles_content(movies):
    content_movie = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content_movie += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content_movie


def open_books_page(books, movies):
    book_tiles=create_book_tiles_content(books)
    movie_tiles=create_movie_tiles_content(movies)
    rendered_content = main_page_content.format(book_tiles=book_tiles, movie_tiles=movie_tiles)
    with open('book_review.html', 'w') as file:
        file.write(main_page_head + rendered_content)

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath('book_review.html')
    webbrowser.open('file://' + url, new=2)

open_books_page(books, movies)
