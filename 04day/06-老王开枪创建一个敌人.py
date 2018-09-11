class Person():
    def __init__(self,name):
        self.name = name
        self.hp = 100

class Gun():
    def __init__(self,name):
        self.name = name

    def zhuangdanjia(self,dj):#装弹夹
        self.dj = dj

class DanJia():
    def __init__(self):
        self.list = []#装子弹
    
    def zhuangzidan(self,zd):
        self.list.append(zd)#装子弹
    
class ZiDan(self):
    def __init__(self):
        self.kill = 5


lw = Person("老王")#创建老王对象
ak47 = Gun("ak47")#创建枪对象
dj = DanJia()#创建一个弹夹
for i in range(30):#创建一些子弹
    zd = ZiDan()
    dj.zhuangzidan(zd)#把子弹装进弹夹
ak47.zhuangdanjia(dj)#把弹夹装到枪上
ls = Person("老宋")#创建一个敌人
