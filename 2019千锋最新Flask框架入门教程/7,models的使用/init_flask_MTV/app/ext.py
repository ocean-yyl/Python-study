from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    db.init_app(app)

    migrate.init_app(app,db) # 两个参数一个是 Flask 的 app，一个是数据库 db