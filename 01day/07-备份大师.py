name = input("请输入要备份的文件的名字")
f = open(name,"r")
content = f.read()
#8.txt ----- 8备份.txt

#8.txt   8 和.txt
#

p = name.rfind(".")#找到.的索引
s = name[:p]
e = name[p:]

newname = s+"备份"+e

f1 = open(newname,"w")
f1.write(content)
f1.close()
f.close()

#把8.txt的内容写入到8备份.txt
#5.txt  5备份.txt
#6.txt  6备份.txt

###
#5.txt  5  .txt   5+"备份"+.txt   
