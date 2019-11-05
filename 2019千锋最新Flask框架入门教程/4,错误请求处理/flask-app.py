from flask import Flask
from flask import Blueprint
app = Flask(__name__)

blue = Blueprint("blue",__name__)


@app.route('/')
def index():
    return "<h1>hello Flask</h1>"

@blue.route("/err")
def errors():
    from flask import abort
    abort(401)

@app.errorhandler(401)
def handle_error401(error):
    return "<h1>401</h1>"

@app.errorhandler(404)
def handle_error404(error):
    return "<h1>没有找到页面,404</h1>"


app.register_blueprint(blue)
if __name__ == '__main__':
    app.run(debug=True)