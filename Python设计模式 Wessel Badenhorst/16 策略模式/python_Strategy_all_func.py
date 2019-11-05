#encoding=utf-8
def executor(arg1,arg2,func=None):
	if func is None:
		print("Strategy is not implemented...")
	else:
		func(arg1,arg2)


def strategy_add(arg1,arg2):
	print(arg1 + arg2)

def strategy_sub(arg1, arg2):
	print(arg1 - arg2)


def main():
	executor(1,2,strategy_add)


if __name__ == '__main__':
	main()