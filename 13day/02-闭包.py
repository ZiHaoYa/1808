'''
def  test():
    print("哈哈哈")

laowang = test
laowang()
test()
'''


def test(num):
    a  = 10
    def test1(x):
        print(x+num)
    return test1
laowang = test(19)
laowang(12)

