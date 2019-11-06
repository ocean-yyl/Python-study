from flask import Flask

app = Flask(__name__)
"""
https://blog.csdn.net/qq_42517220/article/details/88693576

常用路由方式有以下五种
@init_flask_MTV.route('/user/<username>')
@init_flask_MTV.route('/post/<int:post_id>')
@init_flask_MTV.route('/post/<float:post_id>')
@init_flask_MTV.route('/post/<path:path>')
@init_flask_MTV.route('/login', methods=['GET','POST'])

flask路由的规则:
string 接收任何没有斜杠('/')的文件(默认)
path	和默认的相似，但也接受斜线('/')
int	接收整形
float	同int，但是可以接受浮点型
uuid 只接受uuid格式的数据 例如:f0ad9271-13b8-4761-adab-9e51d5c72939
any 穷举

"""
@app.route('/')
def index():
	print(app.url_map)  # 可以通过url_map可以查看整个flask中的路由信息
	return "查看后台"

# 使用url_for 进行url跳转
# url_for('函数名',参数名=value)
# 例如 url_for('user1',id=1881302)
@app.route('/index')
def index2():
	from flask import url_for,redirect
	url = url_for('user1',id=1881302)
	return redirect(url)

@app.route('/user1/<id>/')
def user1(id):
	print(type(id), id)
	return 'Hello: ' + id

@app.route('/user2/<int:id>/')
def user2(id):
	print(type(id), id)
	return 'Hello: ' + str(id)

@app.route('/getuuid/<uuid:uuid>/')
def getuuid(uuid):
	print(type(uuid), uuid)
	return 'Hello: ' + str(uuid)

@app.route('/getany/<any(a,b,c):myany>/')
def getany(myany):
	print(myany)
	return "get any->"+myany


# 自定义装饰器
from werkzeug.routing import BaseConverter
class MobelConverter(BaseConverter):
	""""""
	def __init__(self, url_map):
		# 调用父类的初始化方法
		super().__init__(url_map)
		# 将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
		self.regex = r'1\d{10}'
# 将自定义转换器添加到flask应用中
app.url_map.converters['mobile'] = MobelConverter

# url使用自定义的转换器
@app.route('/phone/<mobile:mobile>')
def send_msg(mobile):
	return 'your phone num is %s' % mobile


# 实现自己的正则表达式转换器
# 定义装饰器
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
	def __init__(self, url_map,my_regex):
		# 调用父类的初始化方法
		super().__init__(url_map)
		# 将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
		self.regex = my_regex
# 将自定义转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter

# url使用自定义的转换器
@app.route("/rephone/<re(r'1[34578]\d{9}'):mobile>")
def rePhone(mobile):
	return 'your phone num is %s' % mobile

if __name__ == '__main__':
	# print(init_flask_MTV.url_map)  # 可以通过url_map可以查看整个flask中的路由信息,命令行输入python manage.py
	app.run(debug=True)
