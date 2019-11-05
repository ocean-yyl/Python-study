#encoding=utf-8
"""使用redis持久化存储session"""
from flask import Flask, session
from flask_session import Session
'https://pythonhosted.org/Flask-Session/'

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'redis' # 配置
app.config.from_object(__name__) # 加载配置

Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

if __name__ == '__main__':
    app.run(debug=True)
