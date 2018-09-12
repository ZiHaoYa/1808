class Animal():
    
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃")

class Dog(Animal):
    def __init__(self):
        self.age = 12

    def eat(self):
        print("吃狗粮")


hsq = Dog()
hsq.eat()
print(hsq.age)
#print(hsq.name)
