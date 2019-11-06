#encoding=utf-8
from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app
import os

env = os.environ.get('FLASK_ENV',"develop")

app = create_app(env)

# cmd控制app
manager = Manager(app)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
