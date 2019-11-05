import time
"""
子程序/函数：在所有的语言中都是层级调用，比如A调用B，B又调用C，在C执行完毕后返回，然后B执行完毕返回，然后A执行完毕。
            这是通过栈实现的，一个线程就是执行一个子程序，子程序调用总是有一个入口，一次返回，调用的顺序是明确的。
            
协程概述：看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，不是函数调用。

与线程相比，协程的执行效率极高，因为只有一个线程，也不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态。

协程原理：Python对协程的支持，是通过generator（生成器）实现的

"""

'''
# 协程的最简单风格，控制函数的阶段执行，节约线程或进程的切换
# 返回一个生成器
def run1():
    print("yield->",1)
    yield 1
    print("yield->",2)
    yield 2
    print("yield->",3)
    yield 3



m = run1()
print(next(m))
print(next(m))
print(next(m))
# print(next(m))
'''

# 协程---数据传输
def run2():
    data = "data"
    print("1---",data)
    data = yield 'x'
    print("2---", data)
    data = yield 'y'
    print("3---", data)
    data = yield 'z'
    print("4---", data)

m2  = run2()
print(next(m2)) # 生成器开始，不可以使用send。
print(m2.send('a'))
print(m2.send('b'))
print(m2.send('c'))
# print(m.send('d'))
