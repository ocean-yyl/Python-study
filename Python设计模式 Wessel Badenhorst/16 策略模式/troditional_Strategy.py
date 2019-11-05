# encoding=utf-8

class StrategyExecutor(object):
	def __init__(self, strategy=None):
		self.strategy = strategy

	def execute(self, arg1, arg2):
		if self.strategy is None:
			print("Strategy is not implemented...")
		else:
			self.strategy.execute(arg1, arg2)


class AddStrategy(object):
	def execute(self, arg1, arg2):
		print(arg1 + arg2)


class SubStrategy(object):
	def execute(self, arg1, arg2):
		print(arg1 - arg2)


def main():
	add_strategy = StrategyExecutor(AddStrategy())
	add_strategy.execute(1, 2)


if __name__ == '__main__':
	main()
"""
至少我们防止了if语句的无序蔓延并且解决了每次添加另一条策略时都需要更新executor函数的问题。
这是通往正确方向所迈出的良好一步。我们的系统变得更为解耦一些,
并且该程序的每个部分仅处理其关心的执行部分,而不需要担心系统的其他元素。
在这一传统实现中,使用了鸭子类型,就像在本书中多次所做的那样。
现在,将使用另一个强大的Python工具来编写干净的代码--就像所有其他值那样使用函数。
这意味着可以将一个函数传递到Executor类,而不必首先在其自己的类中封装该函数。
从长期来看,这样的做法不仅会极大地减少必须编写的代码量,还会让代码更易于阅读并且更易于测试,
因为我们可以将参数传递给函数,并且断言它们会返回我们期望的值。
"""