def line1(a,b):
    def line2(x):
        y = a*x+b
        return y
    return line2

line2 = line1(4,5)
ret = line2(10)
print(ret)
ret1 = line2(11)
ret1 = line2(12)
ret1 = line2(13)
ret1 = line2(14)

def line(a,b,x):
    y = a*x+b

line(4,5,10)
line(4,5,11)
line(4,5,12)
