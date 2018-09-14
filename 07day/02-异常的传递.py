def test1():
    print(num)


def test2():
    test1()

def test3():
    try:
        test2()
    except Exception as ret:
        print("捕获到了")
        print(ret)

test3()
