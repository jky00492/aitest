from aitest import db

class Question(db.Model):
    grpid = db.Column(db.Integer, primary_key=True)
    innerid = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)