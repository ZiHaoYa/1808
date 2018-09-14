class caluDay():
    b_m = [1,3,5,7,8,10,12]
    s_m = [4,6,9,11]
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d
        self.ret = 0#统计天数


    def calu(self):#计算天数
        for i in range(1,self.m):
            print(i)
            if i in caluDay.b_m:
                self.ret+=31
            elif i in caluDay.s_m:
                self.ret+=30
        if self.isYear():
            self.ret+=29
        else:
            self.ret+=28

        self.ret+=self.d
        return self.ret

    def isYear(self):
        if (self.y % 4 == 0 and self.y % 100!=0) or(self.y % 400 == 0):
            return True
        else:
            return False

    @classmethod
    def delDate(cls,date):
        l = date.split("-")
        return cls(int(l[0]),int(l[1]),int(l[2]))
    
        
str = "2018-09-13"
clauday = caluDay.delDate(str)
ret = clauday.calu()
print(ret)
