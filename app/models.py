from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(db.Model):

    pass_secure  = db.Column(db.String(255))

        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    upvote=db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote=db.relationship('Downvote',backref='pitch',lazy='dynamic')
    # comment=db.relationship('comment',backref='pitch',lazy='dynamic')


    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

class Upvote(db.Model):
    __tablename__='upvotes'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))


    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = Pitch.query.filter_by(pitch_id=id).all()
        return upvotes

class Downvote(db.Model):
    __tablename__='downvotes'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvotes = Pitch.query.filter_by(pitch_id=id).all()
        return downvotes
