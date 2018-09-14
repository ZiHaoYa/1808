class Dog(object):
    count  = 0
    def __init__(self):
        self.name = "tom"
        Dog.count+=1
    
    def eat(self):#实例方法
        print("吃")

    @classmethod
    def show(cls):#类方法
        print("---------")

    @staticmethod
    def menu():#静态方法
        print("1、开始")
        print("2、结束")

tom = Dog()
tom.eat()#调用实例方法
tom.show()#用对象调用类方法
Dog.show()#用类调用类方法

Dog.menu()#用类调用静态方法
tom.menu()#用对象调用静态方法

