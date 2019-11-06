from flask import Blueprint,render_template
from app.models import Student


bp = Blueprint("blueprint",__name__)

# ×¢²ábp
def init_bp(app):
    app.register_blueprint(bp)

@bp.route('/')
def index():
    return render_template("./hello.html")

