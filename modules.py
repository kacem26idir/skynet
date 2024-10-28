from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    id = db.Column(db.Ineger, primary_key = True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    profile = db.Column(db.Text)