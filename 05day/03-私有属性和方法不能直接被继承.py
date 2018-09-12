class Animal():
    def __init__(self):
        self.__age = 15

    def getAge(self):#一定能被继承
        return self.__age
   
    def __getAge(self):
        return 20
   
    def getAge1(self):
        return self.__getAge() 
class Dog(Animal):
    pass


hsq = Dog()
#print(hsq.__age)
#hsq.__getAge()
print(hsq.getAge())
print(hsq.getAge1())
