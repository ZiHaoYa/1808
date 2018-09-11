class Dog():
    def __init__(self,name):
        self.name = name
        self.age = 1

    def setAge(self,age):
        if age > 1 and age < 15:
            self.age = age
        else:
            print("不合法")
    def getAge(self):
        return self.age

hsq = Dog("哈士奇")
#hsq.age = 50
hsq.setAge(10)#设置属性

#print(hsq.age)
print(hsq.getAge())




    
