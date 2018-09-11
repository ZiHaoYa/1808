class Dog():
    def __str__(self):#打印对象的会执行
        return "哈哈"

    def __init__(self,name):#初始化属性 创建实例对象的时候会执行
         self.name = name

    def __del__(self):#当对象没有任何变量指向它的时候，会被调用
        print("啊")



hsq = Dog("哈士奇")
hsq1 = hsq
del hsq
del hsq1
print("哈哈")        
    
