#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic  # test3 = makeItalic(test3)
def test3():
    return "hello world-3"

print(test1())#<b>hello world-1</b>
print(test2())#<i>hello world-2</i>
print(test3())#<b><i>hello world-3</i></b>












def test1(num):
	print("haha",num)  #先print("买了佛冷")

test1(1)






