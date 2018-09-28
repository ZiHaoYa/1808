from threading import Thread
import time
num = 0
flag = True
def test1():
    global num
    global flag
    if flag:
        for i in range(1000000):
            num+=1
        flag = False
    print('test1',num)

def test2():
    global num
    global flag
    while True:
        if not flag:
            for i in range(1000000):
                num+=1
            flag = True
            break
    print('test2',num)
t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
#time.sleep(3)
t2.start()
