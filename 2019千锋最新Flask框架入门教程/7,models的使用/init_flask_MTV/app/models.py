from app.ext import db

# 需要在views中引用自定义的Modles
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(10))