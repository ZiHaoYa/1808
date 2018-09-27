def fib():
    a,b = 0,1
    for i in range(10):
        #print(b)
        print("1111111111111111111")
        var = yield b
        print(var)
        print("22222222222222222222222")
        a,b = b,a+b


b = fib()
print(b)
#print(next(b))
#print(next(b))
#print(next(b))

#print(b.__next__())
#print(b.__next__())
#print(b.send("哈哈"))#可以让生成器生成，并且可以传参

print(b.send(None))

