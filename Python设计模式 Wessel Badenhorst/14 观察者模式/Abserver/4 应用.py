# encoding=utf-8
#RPG游戏: 钱包/经验/徽章
# 一旦到达阈值,就会获得正确的徽章奖励.
class Task(object):
	def __init__(self, user, _type):
		self.observers = set()
		self.user = user
		self._type = _type


	def register(self,observer):
		self.observers.add(observer)

	def unregister(self,observer):
		self.observers.discard(observer)

	def unregister_all(self):
		self.observers = set()

	def update_all(self):
		for observer in self.observers:
			observer.update(self)



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

	def update(self,observed):
		self.add_experience(1)

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

	def update(self,observed):
		self.increase_balance(5)

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

	def update(self,observed):
		if observed._type == self._type:
			self.add_points(2)

def main():
	wallet = Wallet()
	user = User(wallet)

	badges = [
		Badge("Fun Badge", 1),
		Badge("Bravery Badge", 2),
		Badge("Missing Badge", 3)
	]
	user.badges.extend(badges)

	tasks = [Task(user, 1), Task(user, 1), Task(user, 3),Task(user, 2)]

	for task in tasks:
		task.register(wallet)
		task.register(user)
		for badge in badges:
			task.register(badge)

	# 完成任务
	for task in tasks:
		task.update_all()

	print(user)


if __name__ == '__main__':
	main()
