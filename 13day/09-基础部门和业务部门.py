#-------基础部门---------------
def f1():
    check_login()
    print("f1")


def f2():
    check_login()
    print("f2")

def check_login():
    #验证
    print("haha")
    pass

#---------业务部门A----------------

f1()
f2()
#----------业务部门B----------------------
f1()
f2()
