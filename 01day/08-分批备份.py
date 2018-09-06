name = input("请输入要备份的文件的名字")
p = name.rfind(".")#找到.的索引
s = name[:p]
e = name[p:]
newname = s+"备份"+e
f = open(name,"r")
f1 = open(newname,"w")
while True:
    content = f.read(1024)
    f1.write(content)
    if len(content) == 0:
        break
f1.close()
f.close()

#把8.txt的内容写入到8备份.txt
#5.txt  5备份.txt
#6.txt  6备份.txt

###
#5.txt  5  .txt   5+"备份"+.txt   
