import random
class DiGua():
    def __init__(self):
        self.status = "生的"
        self.times = 0
        self.zls = []#列表属性 装作料
    def __str__(self):
        msg = "我叫地瓜,我现在的状态是%s,我的作料有%s"%(self.status,self.zls)
        return msg
    def kao(self,time):
        self.times +=time    
        if self.times > 0 and self.times <= 5:
            self.status = "生的"
        elif self.times > 5 and self.times <= 10:
            self.status = "半生不熟"
        elif self.times > 10 and self.times <= 15:
            self.status = "熟了"
        else:
            self.status = "糊了"
    def addzl(self,zl):
        self.zls.append(zl)
dg = DiGua()#创建地瓜对象
zls = ["盐","孜然","胡椒粉","大料","八角","辣椒"]
for i in range(10):
    dg.kao(random.randint(1,3))
    if zls:
        s = random.choice(zls)
        zls.remove(s)#从作料库中删除掉
        dg.addzl(s)
    print(dg)
