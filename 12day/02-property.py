class Dog():

   def __init__(self):
        self.__age = 0

   def setAge(self,age):
        self.__age = age

   def getAge(self):
        return self.__age

   age = property(getAge,setAge)

dog = Dog()
#dog.setAge(10)
#print(dog.getAge())

dog.age = 10#相当于执行16行
print(dog.age)#相当于执行17行

