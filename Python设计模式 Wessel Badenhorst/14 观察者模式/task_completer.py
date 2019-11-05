# encoding=utf-8
#RPG游戏: 钱包/经验/徽章
# 一旦到达阈值,就会获得正确的徽章奖励.
class Task(object):
	def __init__(self, user, _type):
		self.user = user
		self._type = _type

	def complete(self):
		self.user.add_experience(1)
		self.user.wallet.increase_balance(5)

		# badges 徽章
		for badge in self.user.badges:
			if self._type == badge._type:
				badge.add_points(2)

class User(object):
	def __init__(self, wallet):
		self.wallet = wallet # 钱包
		self.badges = [] # 徽章
		self.experience = 0 # 经验

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
这一非常基础的实现具有一组相当复杂的计算,用以在一个任务完成时执行。
在上面的代码中,我们拥有了一种实现得相当完善的架构,不过该评价函数仍旧艮笨拙,
并且我相信大家已经有所体会,这段代码并非我们想要在其运行之后继续改进的代码。
我还认为,为这个方法编写测试代码并非是一件愉悦的事情。
对于该系统的任何添加项都意味着要修改这个方法,这就会迫使我们实现更多的计算和评价。
正如我们之前所说的,这是通向紧耦合系统的征兆。
Task对象必须知道与每个points对象有关的信息,以便能够将正确的积分或荣誉值分配到正确的子系统。
我们希望从task complete方法的主要部分中移除每条规则的评价,
并且让子系统承担更多的职责,这样它们就能基于其自己的规则而非那些具有一定预见性的对象来处理数据变更。
为此,我们要采取通向一种更为松耦合系统的第一步,如这里所示:
task_semi_decoupled.py
"""