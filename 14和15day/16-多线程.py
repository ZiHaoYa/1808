import time
from threading import Thread
def say():
    print("哈哈")
    time.sleep(1)

'''
for i in range(5):
    say()
'''

for i in range(5):
    t = Thread(target=say)
    t.start()
    
