#encoding=utf-8
import time


class RawCalculator(object):
	def fib(self, n):
		print("RawCalculator->init")
		if n < 2:
			return 1
		return self.fib(n - 2) + self.fib(n - 1)


def memorize(fn):
	__cache = {}

	def memorized(*args):
		# return 20
		print("memorized->init")
		key = (fn.__name__, args)
		if key in __cache:
			return __cache[key]
		__cache[key] = fn(*args)
		return __cache[key]

	return memorized


# 这里使用fib方法的记忆法版本memorize函数的memorized方法重写了原来对象RawCalculator的fib方法.
"""
memorized方法逻辑如下:
if key in __cache:
	return __cache[key]
__cache[key] = fn(*args) # 否则cache[key] = fib(n)
	
"""
class CalculatorProxy(object):
	def __init__(self, target):
		self.target = target

		# 这里直接将传入的对象的fib方法换掉了,换成了memorize函数
		fib = getattr(self.target, 'fib')
		setattr(self.target, 'fib', memorize(fib))

	def __getattr__(self, name):
		return getattr(self.target, name)


if __name__ == '__main__':
	calculator = CalculatorProxy(RawCalculator())
	start_time = time.time()
	print(calculator.fib(1))

	fib_sequence = [calculator.fib(x) for x in range(3)]
	print(fib_sequence)
	end_time = time.time()
	print(len(fib_sequence), "->", end_time - start_time)
#35 -> 0.0009987354278564453