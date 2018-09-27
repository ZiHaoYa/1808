def foo(fun):
    print("执行了")
    def fib(*args,**kwargs):
        print("正在装饰中")
        return fun(*args,**kwargs)
    return fib


