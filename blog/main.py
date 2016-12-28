import os
import re
import string
import random
import hashlib
import hmac

import jinja2
import webapp2

from uuid import uuid4
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

secret = 'du.uyX9fE~Tb6.pp&U3D-OsmYO,Gqi$^jS34tzu9'

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_value(value):
    return '{}|{}'.format(value, hmac.new(secret, value).hexdigest())

def check_secure_value(secure_value):
    value = secure_value.split('|')[0]
    if secure_value == make_secure_value(value):
        return value

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def hash_string(name, password, salt = None):
    if not salt:
        salt = make_salt()
    return (hashlib.sha256(name + password + salt).hexdigest(), salt)

def check_secure_password(name, password, hash_):
    salt = hash_.split(',')[1]
    return hash_ == hash_string(name, password, salt)

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

class BlogPost(db.Model):
    title = db.StringProperty(required = True)
    postbody = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br/>')

class UserProfile(db.Model):
    username = db.TextProperty(required = True)
    password = db.StringProperty(required = True)
    posts = db.StringProperty()
    email = db.StringProperty()
    salt = db.StringProperty(required = True)

    @classmethod
    def by_id(cls, uuid):
        return cls.get_by_id(uuid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        return cls.all().filter('name = ', name).get()

    @classmethod
    def register(cls, name, password, email = None):
        password_secure = hash_string(name, password)
        return UserProfile(
            parent = users_key(),
            username = name,
            password = password_secure[0],
            email = email,
            salt = password_secure[1])

    @classmethod
    def login(cls, name, password):
        user = cls.by_name(name)
        if user and valid_password(name, password, user.password):
            return user

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        params['user'] = self.user
        template = jinja_env.get_template(template)
        return template.render(params)

    def render(self, template, **kwargs):
        self.write(render_str(template, **kwargs))

    def set_secure_cookie(self, name, value):
        cookie_value = make_secure_value(value)
        self.response.headers.add_header('Set-Cookie', '{}={}; Path=/'.format(name, cookie_value))

    def read_secure_cookie(self, name):
        cookie_value = self.request.cookies.get(name)
        return cookie_value and check_secure_value(cookie_value)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *args, **kwargs):
        webapp2.RequestHandler.initialize(self, *args, **kwargs)
        uuid = self.read_secure_cookie('user_id')
        self.user = uuid and UserProfile.by_id(int(uuid))

class MainPage(Handler):
    def get(self):
        if self.user:
            posts = BlogPost.all().order('-created')
            self.render('home.jinja2', blogposts = posts, signin = True, name = self.user.username)
        else:
            self.render('home.jinja2', blogposts = [], signin = False, name = '')

class NewPost(Handler):
    def get(self):
        if self.user:
            self.render('new_post.jinja2')
        else:
            self.redirect('/home')

    def post(self):
        if not self.user:
            self.redirect('/home')

        have_error = False
        title = self.request.get('title')
        postbody = self.request.get('postbody')

        params = dict(title = title, postbody = postbody)

        if not title:
            params['error_title'] = 'Please enter a title for your post.'
            have_error = True

        if not postbody:
            params['error_body'] = 'Please enter a body for your post.'
            have_error = True

        if have_error:
            self.render('new_post.jinja2', **params)
        else:
            the_post = BlogPost(parent = blog_key(), title = title, postbody = postbody)
            the_post.put()
            self.redirect('/postlink/{}'.format(the_post.key().id()))

class PostLink(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.redirect('/home')

        self.render('view_post.jinja2', post = post)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class signup(Handler):
    def get(self):
        self.render('user_signup.jinja2')

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        email = self.request.get('email')

        params = dict(username = username, email = email)

        if not valid_username(username):
            params['error_username'] = 'Username must contain only alphanumeric characters and be between 3 and 20 letters long.'
            have_error = True

        if not valid_password(password):
            params['error_password'] = 'Password must be between 3 and 20 letters long.'
            have_error = True
        elif password != confirm:
            params['error_confirm'] = 'Your passwords do not match.'
            have_error = True

        if not valid_email(email):
            params['error_email'] = 'Email was not valid.'
            have_error = True

        user = UserProfile.by_name(username)
        if user:
            params['error_username'] = 'User exists.'
            have_error = True

        if have_error:
            self.render('user_signup.jinja2', **params)
        else:
            the_user = UserProfile.register(username, password, email)
            the_user.put()
            self.login(the_user)
            self.redirect('/home')

class login(Handler):
    def get(self):
        self.render('login.jinja2')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        user = UserProfile.login(username, password)

        params = dict(username = username)

        if not user:
            params['error_username'] = 'Username does not exist.'
            self.render('login.jinja2', **params)
        else:
            self.login(user)
            self.redirect('/home')

class logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/home')

app = webapp2.WSGIApplication([
    ('/home', MainPage),
    ('/newpost', NewPost),
    ('/postlink/([0-9]+)', PostLink),
    ('/signup', signup),
    ('/login', login),
    ('/logout', logout)
], debug=True)
