#encoding=utf-8
class Task(object):
	def __init__(self, user, _type):
		self.user = user
		self._type = _type

	def complete(self):
		self.user.add_experience(1)
		self.user.wallet.increase_balance(5)

		# badges 徽章
		for badge in self.user.badges:
			badge.complete_task(self)


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