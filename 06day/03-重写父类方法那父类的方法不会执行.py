class Animal(object):
    def eat(self):
        print("吃")


class Cat(Animal):
    def eat(self):
        print("猫吃猫粮")


cat = Cat()
cat.eat()
