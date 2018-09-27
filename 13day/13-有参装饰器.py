def foo(fun):
    print("执行了")
    def fib(*args,**kwargs):
        print("正在装饰中")
        fun(*args,**kwargs)
    return fib



@foo
def test1(num,num1,num2):
    print("哈哈哈",num,num1,num2)

test1(10,11,12)    
