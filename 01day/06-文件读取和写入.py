name = input("请输入要读取的文件的名字要加后缀名")
f = open(name,"r")
content = f.read()
print(content)
f.close()


f1 = open("4.txt","w")
f1.write("小蓝我爱你")
f1.close()
