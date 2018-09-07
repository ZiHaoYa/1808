class People:
    def eat(self):#方法
        print("吃")
    def sleep(self):#方法
        print("睡觉")


class Dog:
    

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡觉")


bmr = People()#创建小白的实例
bmr.eat()
bmr.sleep()

jm = Dog()#创建一个金毛的实例
jm.eat()
jm.sleep()



