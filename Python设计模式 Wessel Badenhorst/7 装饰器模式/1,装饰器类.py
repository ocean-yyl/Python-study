import time


class ProfilingDecorator(object):
	def __init__(self,f):
		print("Profiling decorator initiated")
		self.f = f

	def __call__(self, *args):
		print("ProfilingDecorator called")
		start_time = time.time()
		result = self.f(*args)
		end_time = time.time()
		print("Time of the func->{} is {}".format(self.f,end_time-start_time))

		return result

class ToHtmlDecorator(object):
	def __init__(self,f):
		print("ToHtmlDecorator initiated")
		self.f = f
	def __call__(self, *args):
		print("ToHtmlDecorator called")
		return "<html><body>{}</body></html>".format(self.f(*args))

@ToHtmlDecorator
@ProfilingDecorator
def fib(n):
	print("in func->fib")

	if n < 2:
		return
	fibPrev = 1
	fib = 1
	for num in range(2, n):
		time.sleep(1.5)
		fibPrev, fib = fib, fib + fibPrev
	return fib


if __name__ == '__main__':
	n = 5
	print("Fibonacci number for n = {}:{}".format(n, fib(n)))
