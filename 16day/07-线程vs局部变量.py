from threading import Thread
#线程 全局变量共享，修改全局变量非安全
#线程 不共享局部变量，每个线程各有一份
#进程 全局变量不共享 每个进程各有一份
class MyThread(Thread):
    def run(self):
        num = 0
        for i in range(10):
            num+=1
        print(self.name,num)



t1 = MyThread()
t2 = MyThread()

t1.start()
t2.start()
    
