
class ConcreteObserver(object):
	def update(self,observed):
		print("Observing: ",observed)

class Observable(object):
	def __init__(self):
		self.observers = set()

	def register(self,observer):
		self.observers.add(observer)

	def ubregister(self,observer):
		self.observers.discard(observer)
		"""
		discard
		Remove an element from a set if it is a member.
		If the element is not a member, do nothing.
		"""

	def unregister_all(self):
		self.observers = set()

	def update_all(self):
		for observer in self.observers:
			observer.update(self)