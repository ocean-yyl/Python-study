class StrategyExecutor(object):
	def __init__(self, func=None):
		if func is not None:
			self.execute = func

	def execute(self, *args):
		print("Strategy is not implemented...")



def strategy_add(arg1,arg2):
	print(arg1 + arg2)

def strategy_sub(arg1, arg2):
	print(arg1 - arg2)



def main():
	add_strategy = StrategyExecutor(strategy_add)
	add_strategy.execute(1, 2)


if __name__ == '__main__':
	main()