class Cat():
    
    def __init__(self,name,age):#初始化属性方法
        self.name = name #添加一个属性
        self.age = age
        print("哈哈")
    def sleep(self):
        print("睡觉")

tom = Cat('tom',8)#默认执行init 
#tom.name = "tom"
tom.sleep()
print(tom.name)
print(tom.age)
