class Book():
    '''
    Creates a book object that can be used to populate a web page
    Inputs:
    - title: the title of the book [str]
    - author: the author of the book [str]
    - series: the series the book belongs to or None [str]
    - review_text: a short blurb about the book [str]
    - image_url: a place to find the cover image of the book [str]
    '''
    def __init__(self, title, author, series, review_text, image_url):
        self.title = title
        self.author = author
        self.series = series
        self.review_text = review_text
        self.image_url = image_url
    
    def create_book_info(self):
        if self.series == None:
            self.series = 'This is a stand alone book.'
        else:
            self.series = 'This book is part of the series {}'.format(self.series)
        return {
            'title': self.title,
            'author': self.author,
            'series': self.series,
            'review_text': self.review_text,
            'image_url': self.image_url
            }


class Movie():
    '''
    Creates a book object that can be used to populate a web page
    Inputs:
    - title: the title of the book [str]
    - author: the author of the book [str]
    - series: the series the book belongs to or None [str]
    - review_text: a short blurb about the book [str]
    - image_url: a place to find the cover image of the book [str]
    '''
    def __init__(self, title, image_url, trailer_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    def create_movie_info(self):
        return {
            'title': self.title,
            'image_url': self.image_url,
            'trailer_url': self.trailer_url
            }
