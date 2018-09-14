class showError(Exception):#Exception是异常的顶级父类   
    def __init__(self,name):
        super().__init__()#加上
        self.name = name
        self.error = "input %s is error"%(self.name)



try:
    name = input("请输入一个名字")
    if name == "老王":
        raise showError(name)
except showError as ret:
    print(ret.error)    
    #输入老王就报错
