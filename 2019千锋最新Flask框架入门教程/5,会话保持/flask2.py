from flask import Flask
from flask import Blueprint
app = Flask(__name__)

blue = Blueprint("blue",__name__)

from flask import make_response,request,session

"""cookies"""
@blue.route("/setcookie")
def set_cookie():
    resp = make_response('set a cookie of username')
    resp.set_cookie("username","psman",max_age=0)
    return resp

@blue.route("/getcookie")
def get_cookie():
    resp = request.cookies.get("username")
    return "getcookie->username : "+resp

"""Sessions"""
# 在服务器端进行状态保持的方案就是Session
# Session依赖于Cookie
app.secret_key = "123456789s"  # 只有设置了secret_key才可以使用session
@blue.route("/setsession")
def set_session():
    session['pwd'] = '123456'
    resp = make_response('set a session of pwd')
    return resp

@blue.route("/getsession")
def get_session():
    sess = session.get("pwd")
    return "getsession->pwd : "+sess


app.register_blueprint(blue)
if __name__ == '__main__':
    app.run(debug=True)