class Person():
    #不想让人直接访问或直接获取的属性可以写成私有属性
    def __init__(self,name):
        self.name = name#公有属性
        self.__mimi = "我处过10个女朋友"#私有属性
        self.__sifangqian = 100

    def getMi(self):#公有方法
        return self.__mimi

    def getMoney(self):#间接的获取私有属性
        return self.__sifangqian

lz  = Person("老赵")
#print(lz.mimi)#不能访问私有属性
print(lz.getMi())#通过公有方法间接访问私有属性
print(lz.getMoney())
