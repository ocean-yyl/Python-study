from functools import wraps


def dummy_decorator(f):
	@wraps(f)
	def wrap_f():
		print("Func to be decorated: ",f.__name__,f)
		print("Nested wrapping func: ",wrap_f.__name__,wrap_f)
		return f()

	return wrap_f


@dummy_decorator
def do_nothing():
	print("Inside do_nothing")


if __name__ == '__main__':
	print("Wrapped func:", do_nothing.__name__,do_nothing)

	do_nothing()
