class Animal(object):
    def __init__(self,name):
        self.name = name   
        self.age = 5
    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Person(Animal):
    pass

tom = Cat("tom")
hsq = Dog("hsq")
tom.eat()
tom.sleep()

hsq.eat()
hsq.sleep()


print(tom.name)
print(hsq.name)
print(tom.age)
print(hsq.age)
