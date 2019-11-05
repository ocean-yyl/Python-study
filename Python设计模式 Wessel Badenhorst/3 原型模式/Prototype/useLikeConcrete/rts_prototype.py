#encoding=utf-8
from prototype_1 import Prototype
from copy import deepcopy


# Knight 骑士
class Knight(Prototype):
	# 这个是关键
	def clone(self):
		return deepcopy(self)

	def __init__(self, level):
		self.unit_type = "Knight"

		filename = "{}_{}.dat".format(self.unit_type, level)

		with open(filename, "r", encoding="utf-8") as parameter_f:
			lines = parameter_f.read().split("\n")
			self.life = lines[0]
			self.speed = lines[1]
			self.attack_power = lines[2]
			self.attack_range = lines[3]
			self.weapon = lines[4]

	def __str__(self):
		return "Type:{0}\n" \
			   "Life:{1}\n" \
			   "Speed:{2}\n" \
			   "Attack_power:{3}\n" \
			   "Attack_range:{4}\n" \
			   "Weapon:{5}\n".format(
			self.unit_type,
			self.life,
			self.speed,
			self.attack_power,
			self.attack_range,
			self.weapon
		)


# archer 射手
class Archer(Prototype):
	# 这个是关键
	def clone(self):
		return deepcopy(self)

	def __init__(self, level):
		self.unit_type = "Archer"

		filename = "{}_{}.dat".format(self.unit_type, level)

		with open(filename, "r", encoding="utf-8") as parameter_f:
			lines = parameter_f.read().split("\n")
			self.life = lines[0]
			self.speed = lines[1]
			self.attack_power = lines[2]
			self.attack_range = lines[3]
			self.weapon = lines[4]

	def __str__(self):
		return "Type:{0}\n" \
			   "Life:{1}\n" \
			   "Speed:{2}\n" \
			   "Attack_power:{3}\n" \
			   "Attack_range:{4}\n" \
			   "Weapon:{5}\n".format(
			self.unit_type,
			self.life,
			self.speed,
			self.attack_power,
			self.attack_range,
			self.weapon
		)


# house 房屋
class House(object):

	def __init__(self):
		self.units = {
			"knight": {
				1: Knight(1),
				2: Knight(2)
			},
			"archer": {
				1: Archer(1),
				2: Archer(2)
			}
		}

	def build_unit(self, unit_type, level):
		"""调用其clone函数,返回"""
		return self.units[unit_type][level].clone()


if __name__ == '__main__':
	house = House()
	knight1 = house.build_unit("knight",2)
	archer1 = house.build_unit("archer",1)
	print(knight1)
	print(archer1)