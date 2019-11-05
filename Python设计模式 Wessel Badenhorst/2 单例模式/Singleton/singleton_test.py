from Singleton.singleton_obj import SingletonObj

obj1 = SingletonObj()
obj1.val = "Obj value = 1"


print("obj1:",obj1,obj1.val)
print("-------")


obj2 = SingletonObj()
obj2.val = "Obj value = 2"
print("obj1:",obj1,obj1.val)
print("obj2:",obj2,obj2.val)
print("-----------")


obj3 = SingletonObj()
obj3.val = "Obj value = 3"
print("obj1:",obj1,obj1.val)
print("obj2:",obj2,obj2.val)
print("obj3:",obj3,obj3.val)