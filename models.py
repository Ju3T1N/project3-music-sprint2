# models.py
from app import DB
from sqlalchemy.dialects import postgresql


class Posts(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(256))
    music = DB.Column(DB.String(120))
    message = DB.Column(DB.String(256))
    title = DB.Column(DB.String(120))
    num_likes = DB.Column(DB.Integer)
    datetime = DB.Column(DB.DateTime)
    

    def __init__(self, username, music, message, title, num_likes, datetime):
        self.username = username
        self.music = music
        self.message = message
        self.title = title
        self.num_likes = num_likes
        self.datetime = datetime

    def __repr__(self):
        return "<Posts: %s>" % self.message


class Comments(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(256))
    text = DB.Column(DB.String(256))
    post_id = DB.Column(DB.Integer)
    datetime = DB.Column(DB.DateTime)

    def __init__(self, username, text, post_id, datetime):
        self.username = username
        self.text = text
        self.post_id = post_id
        self.datetime = datetime

    def __repr__(self):
        return "<Comment name: {}\ntext:{}\post_id: {}".format(
            self.username, self.text, self.post_id
        )


class Users(DB.Model):
    username = DB.Column(DB.String(256), primary_key=True)
    profile_picture = DB.Column(DB.String(256))
    user_type = DB.Column(DB.Integer)
    top_artists = DB.Column(postgresql.ARRAY(DB.String))
    following = DB.Column(postgresql.ARRAY(DB.String))
    my_likes = DB.Column(postgresql.ARRAY(DB.Integer))

    def __init__(self, username, profile_picture, user_type, top_artists, following, my_likes):
        self.username = username
        self.profile_picture = profile_picture
        self.user_type = user_type
        self.top_artists = top_artists
        self.following = following
        self.my_likes = my_likes

    def __repr__(self):
        return "<Users name: {}".format(self.username)

