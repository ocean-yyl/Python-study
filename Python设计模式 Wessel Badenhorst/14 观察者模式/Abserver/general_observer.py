# encoding=utf-8
class ConcreteObserver(object):
	def update(self, observed):
		print("Observing: ", observed)


class Observable(object):
	def __init__(self):
		self.callbacks = set()

	def register(self, callback):
		self.callbacks.add(callback)

	def ubregister(self, callback):
		self.callbacks.discard(callback)
		"""
		discard
		Remove an element from a set if it is a member.
		If the element is not a member, do nothing.
		"""

	def unregister_all(self):
		self.callbacks = set()

	def update_all(self):
		for callback in self.callbacks:
			callback(self)


def main():
	observed = Observable()  # 被观察者
	observer1 = ConcreteObserver()  # 观察者1

	observed.register(lambda x: observer1.update(x))
	observed.update_all()


if __name__ == '__main__':
	main()
