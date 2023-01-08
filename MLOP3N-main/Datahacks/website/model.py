from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50),nullable=False,unique=True)
    phone = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(50), nullable=False)
    
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10),nullable=False)
    open = db.Column(db.String(50),nullable=False)
    close = db.Column(db.String(50),nullable=False)
    high = db.Column(db.String(50),nullable=False)
    low = db.Column(db.String(50),nullable=False)
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))

