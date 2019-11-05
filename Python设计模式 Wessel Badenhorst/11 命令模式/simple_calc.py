class AddCommand(object):
	def __init__(self, receiver, value):
		self.receiver = receiver
		self.value = value

	def execute(self):
		self.receiver.add(self.value)

	def undo(self):
		self.receiver.sub(self.value)


class SubtractCommand(object):
	def __init__(self, receiver, value):
		self.receiver = receiver
		self.value = value

	def execute(self):
		self.receiver.sub(self.value)

	def undo(self):
		self.receiver.add(self.value)


class CalcInvoker(object):
	def __init__(self):
		self.commands = []
		self.undo_stack = []

	def add_new_command(self, command):
		self.commands.append(command)

	def run(self):
		for command in self.commands:
			command.execute()
			self.undo_stack.append(command)

	def undo(self):
		undo_cmd = self.undo_stack.pop()
		undo_cmd.undo()


class Accumulator(object):
	def __init__(self, value):
		self._value = value

	def add(self, value):
		self._value += value

	def sub(self, value):
		self._value -= value

	def __str__(self):
		return "Value:{}".format(self._value)


if __name__ == '__main__':
	acc = Accumulator(10.0)

	invoker = CalcInvoker()
	invoker.add_new_command(AddCommand(acc, 11))
	invoker.add_new_command(AddCommand(acc, 12))
	invoker.add_new_command(SubtractCommand(acc, 10))
	invoker.add_new_command(AddCommand(acc, 11))

	invoker.run()

	print(acc)

	invoker.undo()

	print(acc)

	invoker.undo()

	print(acc)
	invoker.undo()

	print(acc)