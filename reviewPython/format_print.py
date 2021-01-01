x = 10 * 3.25
y = 200 * 200
out1 = (x, y, ('Google', 'Runoob'))
print(out1,type(out1))
print(repr(out1),type(repr(out1)))

print("+"*60)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))
"""
    这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
    还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
    另一个方法 zfill(), 它会在数字的左边填充 0
    """

print("+"*60)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
"""
在括号中的数字(:之前的数字)用于指向传入对象在 format() 中的位置。
如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数，位置及关键字参数可以任意的结合。

可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
>>>import math
>>>print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> for name, number in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, number))
...
Google     ==>          1
Runoob     ==>          2
Taobao     ==>          3


如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
Runoob: 2; Google: 1; Taobao: 3
也可以通过在 table 变量前使用 ** 来实现相同的功能：
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
Runoob: 2; Google: 1; Taobao: 3

% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 
而将右边的代入, 然后返回格式化后的字符串. 例如:
>>> import math
>>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
常量 PI 的值近似为：3.142。
因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().

"""
