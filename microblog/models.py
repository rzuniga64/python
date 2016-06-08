from init import db, app
import datetime
import hashlib


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    pw_hash = db.Column(db.String(64))
    email = db.Column(db.String(100), unique=True) # Used mainly for gravatar.
    location = db.Column(db.String(100))
    bio = db.Column(db.String(1000))

    @property
    def grav_hash(self):
        hash = hashlib.md5()
        hash.update(self.email.strip().lower().encode('utf8'))
        return hash.hexdigest()


class Follow(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # using 'foreign_keys' b/c we have 2 of them
    follower = db.relationship('User', foreign_keys=[follower_id])
    followee = db.relationship('User', foreign_keys=[followee_id])


class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    url = db.Column(db.String(100))
    post = db.Column(db.String(256))
    # avatar is omitted since this can be obtained from the User model corresponding to the creator.
    photo = db.Column(db.BLOB)
    photo_type = db.Column(db.String(50))

    creator = db.relationship('User', foreign_keys=[creator_id],
                              backref=db.backref('posts', lazy='dynamic'))
    # omitting recipient information since posts are not directed to specific receivers.
    # Whether a user sees a post will be determined by whether or not they follow the poster.

    @property
    def jsonable(self):
        return {
            'post_id': self.id,
            'timestamp': str(self.timestamp),
            'url': self.url,
            'text': self.post,
            'creator': self.creator.name,
            'grav_hash': self.creator.grav_hash
        }


# This creates a list of which users a User follows.
User.followees = db.relationship('User', secondary='follow',
                                 primaryjoin=User.id == Follow.follower_id,
                                 secondaryjoin=User.id == Follow.followee_id)

db.create_all(app=app)