class Test():

    def __init__(self,fun):
        self.fun = fun
    def __call__(self):#对象()
        print("哈哈")
        self.fun()


@Test        #test1 = Test(test1)#相当于创建一个对象让test1引用
def test1():
    print("test")


test1()#相当于对象()
