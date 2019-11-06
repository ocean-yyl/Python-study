from flask import Flask

from app.views import init_bp
from app.settings import envs
from app.ext import init_ext

def create_app(env):
    app = Flask(__name__,template_folder='../templates')

    # ≈‰÷√
    app.config.from_object(envs.get(env))

    # ¿©’πø‚
    init_ext(app)

    # ¬∑”…
    init_bp(app)


    return app