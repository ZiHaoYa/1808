import os
import time
num = 0
pid = os.fork()
if pid == 0:
    time.sleep(3)
    if num == 1:
        print("通信")
    print("子进程",num)
else:
    num+=1
    print("父进程",num)

#进程间不共享全局变量，全局也不能当做进程间通信
#
