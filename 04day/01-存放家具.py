class Home():
    def __init__(self,address,area,type):
        self.address = address#地址
        self.area = area#面积
        self.type = type#户型
        self.list = []#装家具
    def __str__(self):
        msg = "我老家在%s,我的床有%d个"%(self.address,len(self.list))
        return msg
    
    def ban(self,jiaju):
        #先判断一下房子剩余多少面积
        all = 0
        for bed in self.list:#计算所有面积
            all+=bed.area
        diff = self.area - all #剩余面积
        print("剩余%d"%diff)
        if diff >= jiaju.area:
            self.list.append(jiaju)#把家具放到列表中
        else:
            print("不够了")
class JiaJu():
    def __init__(self,area,name):
        self.area = area
        self.name = name

lxl = Home("北京市长安街666号",1500,'八室八厅')#创建实例对象 会执行init方法 

bed = JiaJu(50,"席梦思")
for i in range(40):
    lxl.ban(bed)
#如果无限往房间里面加床，如果房间满就不能再往里加了
print(lxl)#打印对象会执行str方法
