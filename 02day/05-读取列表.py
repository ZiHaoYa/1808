list = []
f = open("data.data","r")
#eval 你存的真正的类型，转换成什么类型
list = eval(f.read())
print(list)
print(type(list))
f.close()
