#encoding=utf-8
from flask import Flask
from flask import Blueprint
app = Flask(__name__)

blue = Blueprint("blue",__name__)

from flask import render_template
@app.route('/')
def index():
    return render_template("index.html",phone="1881302")



app.register_blueprint(blue)
if __name__ == '__main__':
    app.run(debug=True)