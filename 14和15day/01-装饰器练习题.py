import time
def test(fun):
    def f1(*args,**kwargs):
        with open('1.txt','a') as f:
            f.write(time.strftime("%Y-%m-%d %X")+fun.__name__+"\n")
        return fun(*args,**kwargs)
    return f1


@test
def test1():
    print("test1")

test1()






