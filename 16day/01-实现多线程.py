from threading import Thread
import time

def sing():
    for i in range(10):
        time.sleep(1)
        print("唱歌")

def dance():
    for i in range(10):
        time.sleep(1)
        print("跳舞")

t1 = Thread(target=sing)
t2 = Thread(target=dance)

t1.start()
t2.start()
    





