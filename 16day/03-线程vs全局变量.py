from threading import Thread
import time
num = 0
def test1():
    global num
    time.sleep(1)
    num+=1
    print("test1",num)

def test2():
    time.sleep(5)
    print('test2',num)

t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
t2.start()


