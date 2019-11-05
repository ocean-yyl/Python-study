import threading
import time
"""
进程之间变量不共享。每一个进程都有自己的堆栈（内存），各自分配有自己的资源。一般来说，进程之间的运行互不影响。要实现进程之间的通信，可以使用队列。

线程之间变量共享.线程通常叫做轻型的进程，线程是共享内存的并发执行的任务，每个线程都公用一个资源。

进程启动时会默认启动一个主线程，主线程可以启动新的子线程。
"""

class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "子线程"+self.name+'执行，i='+str(i) #name属性中保存的是当前线程的名字
            print(msg)
if __name__ == '__main__':
    print('-----主线程开始-----')
    t1 = SubThread() # 创建子线程t1
    t2 = SubThread() # 创建子线程t2
    t1.start()      # 启动子线程t1
    t2.start()      # 启动子线程t2
    t1.join()       # 等待子线程t1
    t2.join()       # 等待子线程t2
    print('-----主线程结束-----')