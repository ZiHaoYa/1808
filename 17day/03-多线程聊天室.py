from threading import Thread
from socket import *
#配置信息
#1、对方ip
#2、对方端口
#创建一个udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',8888))
ip = input("请输入对方ip地址")
port = int(input("请输入对方端口"))
def send():
	while True:
		print(ip,port)
		content = input("请输入发送消息")
		s.sendto(content.encode('gb2312'),(ip,port))
		print("呵呵")

def recv():
	while True:
		msg = s.recvfrom(1024)
		print(msg[0].decode("gb2312"))

#创建两个线程

t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()
t1.join()
t2.join()




