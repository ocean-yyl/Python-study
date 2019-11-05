import time


def profiling_deroctor(f):
	print("profiling_deroctor called")
	def wrapped_f(n):
		print("profiling_deroctor->wrapped_f called")
		start_time = time.time()
		result = f(n)
		end_time = time.time()
		print("Time of the func->{} is {}".format(f, end_time - start_time))

		return result

	print("before (return wrapped_f)...")
	return wrapped_f

@profiling_deroctor
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
	print("Fibonacci number for n = {} is:{}".format(n, fib(n)))
