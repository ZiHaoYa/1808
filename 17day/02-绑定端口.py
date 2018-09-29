from socket import *
#创建一个udp的套接字
#AF_INET -----IPV4
#SOCK_DGRAM ----UDP
s = socket(AF_INET,SOCK_DGRAM)

#绑定端口
s.bind(('',8888))
s.sendto("你好".encode('gb2312'),('172.20.10.2',8080))
while True:
	msg = s.recvfrom(1024)
	print(msg[0].decode('gb2312'),msg[1][0])
s.close()


