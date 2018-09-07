import os
name = input("请输入文件夹名字")
files = os.listdir(name)
print(os.getcwd())
os.chdir(name)#切换路径
print(os.getcwd())#打印路径
for i in files:
    p = i.rfind('.')
    s = i[:p]
    e = i[p:]
    nn = s+"啊哈哈"+e
    os.rename(i,nn)#重命名
    


















    oldname = './'+name+"/"+i
    #/Users/xiaoyuan/Desktop/1808/02day/mimi/01.xxx
    newname = './'+name+"/"+nn
    print(oldname)
    print(newname)
    os.rename(oldname,newname)
#把文件夹里面的所有文件列出来  返回列表

#遍历列表
    #重命名 
    #01.avi  ----- 01精品.avi
    #02.txt ------ 02精品.txt
   



