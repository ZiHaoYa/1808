def a():
    while True:
        print("哈哈")
        yield None


def b():
    while True:
        print("呵呵")
        yield None


g1 = a()
g2 = b()

while True:
    next(g1)
    next(g2)



