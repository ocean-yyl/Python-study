#encoding=utf-8
class Task(object):
	def __init__(self, user, _type):
		self.user = user
		self._type = _type
		self.callbacks = [
			self.user,
			self.user.wallet
		]
		self.callbacks.extend(self.user.badges)
	def complete(self):
		for item in self.callbacks:
			item.complete_task(self)


class User(object):
	def __init__(self, wallet):
		self.wallet = wallet # 钱包
		self.badges = [] # 徽章
		self.experience = 0 # 经验

	def complete_task(self,task):
		self.add_experience(1)

	def add_experience(self, amount):
		self.experience += amount

	def __str__(self):
		return "Wallet\t{}\n" \
			   "Experience\t{}\n" \
			   "Badges\t{}\n".format(
			self.wallet,
			self.experience,
			"\n".join([str(x) for x in self.badges])
		)

# 钱包
class Wallet(object):
	def __init__(self):
		self.amount = 0

	def increase_balance(self, amount):
		self.amount += amount

	def complete_task(self,task):
		self.increase_balance(5)

	def decrease_balance(self, amount):
		self.amount -= amount

	def __str__(self):
		return str(self.amount)


# 徽章
class Badge(object):
	def __init__(self, name, _type):
		self.points = 0
		self.name = name
		self._type = _type
		self.awarded = False

	def add_points(self, amount):
		self.points += amount
		if self.points > 3:
			self.awarded = True

	def complete_task(self, task):
		if task._type == self._type:
			self.add_points(2)

	def __str__(self):
		if self.awarded:
			award_str = "获奖"
		else:
			award_str = "未获奖"

		return "{}:{} [{}]".format(
			self.name,
			award_str,
			self.points
		)

def main():
	wallet = Wallet()
	user = User(wallet)

	user.badges.append(Badge("Fun Badge", 1))
	user.badges.append(Badge("Bravery Badge", 2))
	user.badges.append(Badge("Missing Badge", 3))

	tasks = [Task(user, 1), Task(user, 1), Task(user, 3),Task(user, 2)]

	# 完成任务
	for task in tasks:
		task.complete()

	print(user)


if __name__ == '__main__':
	main()

"""
现在我们拥有了一列在任务完成时进行回调的对象,
并且该任务不需要知晓与该回调列表中对象有关的任何更多信息,不过前提是这些对象要有一个 complete task0)方法,
该方法要采用刚刚完成的任务作为参数。
无论我们何时希望将调用的源从被调用代码中动态解耦出来,这都是适用的方式。

这个问题是另一个非常常见的问题之一,它是如此之常见以至于另一种设计模式应运而生一观察者模式。
如果从我们正研究的问题回退一步并且大致思考这个观察者模式,那么它看起来就会像这样。
该模式中有两类对象,一个Observable类,(可观察的)
它可以被其他类观察,还有一个 Observer类,(观察者)
当这两个类所连接到的Observable对象正在发生变更时,将会对 Observer类发出警告。
"""
