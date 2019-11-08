#encoding=utf-8
from flask import Blueprint,render_template
from app.models import Student,User
from app.ext import db

bp = Blueprint("blueprint",__name__,template_folder="../templates",url_prefix="/blue")

# 注册bp
def init_bp(app):
    app.register_blueprint(bp)

@bp.route('/')
def index():
    return render_template("./hello.html")

# 插入一个
@bp.route('/adduser')
def adduser():
    user = User()
    user.name = "psman"
    user.uid = 16301

    db.session.add(user)
    db.session.commit()

    return "增加User ok"

# 批量插入
@bp.route('/addusers')
def addusers():
    userlist = []
    for i in range(10,20):
        user = User()
        user.name = "psman"+str(i)
        user.uid = 10000+i
        userlist.append(user)

    db.session.add_all(userlist)
    db.session.commit()

    return "增加10*users ok"

# 获取所有
@bp.route('/getusers')
def getuser():
    users = User.query.all()

    return render_template("hello.html",users=users)

#update
@bp.route('/update')
def updateuser():
    user = User.query.first()
    user.name = user.name+"UU"
    db.session.add(user)
    db.session.commit()

    return "update成功:" + user.name

# 删除
@bp.route('/del')
def deleteuser():
    user = User.query.first()

    db.session.delete(user)
    db.session.commit()

    return "删除成功:"+user.name