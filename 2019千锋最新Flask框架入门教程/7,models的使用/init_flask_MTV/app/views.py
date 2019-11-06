#encoding=utf-8
from flask import Blueprint,render_template
from app.models import Student,User
from app.ext import db

bp = Blueprint("blueprint",__name__)

# 注册bp
def init_bp(app):
    app.register_blueprint(bp)

@bp.route('/')
def index():
    return render_template("./hello.html")

@bp.route('/adduser')
def adduser():
    user = User()
    user.name = "psman"
    user.uid = 16301

    db.session.add(user)
    db.session.commit()

    return "增加User ok"

@bp.route('/getuser')
def getuser():
    users = User.query.all()

    print(users)
    return "ok"