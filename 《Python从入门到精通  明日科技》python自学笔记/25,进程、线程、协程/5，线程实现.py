import threading
import time
"""
进程之间变量不共享。每一个进程都有自己的堆栈（内存），各自分配有自己的资源。一般来说，进程之间的运行互不影响。要实现进程之间的通信，可以使用队列。

线程之间变量共享.线程通常叫做轻型的进程，线程是共享内存的并发执行的任务，每个线程都公用一个资源。

进程启动时会默认启动一个主线程，主线程可以启动新的子线程。
"""

def run(id):
    print("子线程%s 开始，线程名称：%s" % (id,threading.current_thread().name))
    time.sleep(2) # 睡眠2秒
    print("子线程%s 结束，线程名称：%s" % (id,threading.current_thread().name))

if __name__ == '__main__':
    print("主线程%s开始" % threading.current_thread().name)

    for i in range(10):
        t = threading.Thread(target=run,args=(i,),name="my-thread-name-"+str(i))
        t.start()
        # t.join()
    print("主线程%s结束" % threading.current_thread().name)
