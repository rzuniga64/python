from init import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(20))
    pw_hash = db.Column(db.String(64))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(50))
    question = db.Column(db.String(1000))
    date_asked = db.Column(db.String(20))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    creator = db.relationship('User', backref='questions')


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    answer = db.Column(db.String(1000))

    creator = db.relationship('User', backref='answers')
    question = db.relationship('Question', backref='answers')

class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))

    creator = db.relationship('User', backref='upvotes')
    answer = db.relationship('Answer', backref='upvotes')

class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))

    creator = db.relationship('User', backref='downvotes')
    answer = db.relationship('Answer', backref='downvotes')


class QuestionTag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    tag = db.Column(db.String(50))

    question = db.relationship('Question', backref='tags')

db.create_all(app=app)
