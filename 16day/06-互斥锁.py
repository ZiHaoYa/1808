from threading import Thread,Lock
import time
num = 0
def test1():
    global num
    for i in range(1000000):
        m.acquire()#抢锁
        num+=1
        m.release()#释放锁
    print('test1',num)

def test2():
    global num
    for i in range(1000000):
        m.acquire()
        num+=1
        m.release()
    print('test2',num)
m = Lock()
t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
#time.sleep(3)
t2.start()
