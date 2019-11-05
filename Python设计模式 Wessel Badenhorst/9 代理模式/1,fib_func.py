import time


def fib(n):
	if n < 2:
		return 1
	return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
	start_time = time.time()
	fib_sequence = [fib(x) for x in range(1, 35)]
	end_time = time.time()
	print(len(fib_sequence), "->", end_time - start_time)
#34 -> 10.751258850097656