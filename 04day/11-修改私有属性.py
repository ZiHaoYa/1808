class Women():
    def __init__(self):
        self.__age = 50

    def getAge(self):
        return self.__age
    
    def setAge(self,age):#修改私有属性
        self.__age = age

wm = Women()
print(wm.getAge())

wm.setAge(20)
print(wm.getAge())


    


