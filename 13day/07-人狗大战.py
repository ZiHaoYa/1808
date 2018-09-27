class Animal():
    def __init__(self):
        self.hp = 100

class Person(Animal):

    def da(self,obj):
        obj.hp -= 10

    def __str__(self):
        return str(self.hp)

class Dog(Animal):
    def yao(self,obj):
        obj.hp -= 20

    def __str__(self):
        return str(self.hp)

dog = Dog()
p = Person()
p.da(dog)
p.da(dog)
p.da(dog)
dog.yao(p)
dog.yao(p)
dog.yao(p)
print(p)
print(dog)
