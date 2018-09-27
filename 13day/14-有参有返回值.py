def foo(fun):
    print("执行了")
    def fib(*args,**kwargs):
        print("正在装饰中")
        return fun(*args,**kwargs)
    return fib



@foo
def test1(num,num1,num2):
    print("哈哈哈",num,num1,num2)
    return "呵呵"

ret = test1(10,11,12)    
print(ret)

@foo
def test2():
    print("哈哈哈")

test2()

@foo
def test3(num):
    print(num)

test3(10)

@foo
def test4():
    return "hehe"

print(test4())
