class Dog(object):
    flag = True#类属性 默认第一次
    obj = None#类属性 用来保存对象
    def __new__(cls):
        if cls.flag:
            cls.obj = super().__new__(cls)#把对象保存起来
            cls.flag = False
            return cls.obj
        else:
            #把保存的对象之间返回 不需要创建
            return cls.obj

dog = Dog()
print(id(dog))
dog1 = Dog()
print(id(dog1))
