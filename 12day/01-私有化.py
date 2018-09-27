from test import *
class Dog():

    def __show(self):
        print("这是私有方法")

    def __init__(self):
        print("魔法方法")


dog = Dog()
print(dir(Dog))
dog._Dog__show()
#dog.__show()#不能直接

print(a)
#print(_b)
#print(__c)
