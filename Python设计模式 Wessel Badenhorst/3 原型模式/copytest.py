#encoding=utf-8

#1,浅拷贝
"""
a = list(range(1,6))
print("[a] {}".format(a))

b = a
print("[b] {}".format(b))

b.append(0)
print("[a] {}".format(a))
print("[b] {}".format(b))
"""


#2,一层深度拷贝a[:]即a.copy()
#仅会复制列表的第一层级上的元素,第二层级list的结构不会被复制,
#而仅仅相当于引用了其地址而已,也就是浅拷贝.
"""
a = list(range(1,6))
print("[a] {}".format(a))

b = a[:]
print("[b] {}".format(b))

b.append(0)
print("[a] {}".format(a))
print("[b] {}".format(b))

# 处理嵌套结构时
a2 = [1,2,3,["a","b","c"]]
print("[a2] {}".format(a2))

b2 = a2[:]
print("[b2] {}".format(b2))

b2[3][0] = "should changed"
print("[a2] {}".format(a2))
print("[b2] {}".format(b2))

'''
# 使用b = a[:]与b = a.copy(),是完全相当的操作
a = list(range(1,6))
print("[a] {}".format(a))

b = a[:]
print("[b] {}".format(b))

b.append(0)
print("[a] {}".format(a))
print("[b] {}".format(b))

# 处理嵌套结构时
a2 = [1,2,3,["a","b","c"]]
print("[a2] {}".format(a2))

b2 = a2.copy()
print("[b2] {}".format(b2))

b2[3][0] = "should changed"
print("[a2] {}".format(a2))
print("[b2] {}".format(b2))
'''


"""


#3, 深拷贝
# 它允许对任意列表进行完整的深拷贝
from copy import deepcopy
a = list(range(1,6))
print("[a] {}".format(a))

b = a[:]
print("[b] {}".format(b))

b.append(0)
print("[a] {}".format(a))
print("[b] {}".format(b))

# 处理嵌套结构时
a2 = [1,2,3,["a","b","c"]]
print("[a2] {}".format(a2))

b2 = deepcopy(a2)
print("[b2] {}".format(b2))

b2[3][0] = "should changed"
print("[a2] {}".format(a2))
print("[b2] {}".format(b2))