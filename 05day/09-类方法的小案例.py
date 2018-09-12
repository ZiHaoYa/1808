class Tool():
    '''
    格式化输出时间
    '''
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d
   
    def out(self):
        print("今年是%s年%s月%s日"%(self.y,self.m,self.d))


    @classmethod
    def delDate(cls,date):
        l = str.split("-")
        y = l[0]
        m = l[1]
        d = l[2]
        #return y,m,d 
        #return cls(y,m,d)  #cls = Tool    Tool(y,m,d)  = cls(y,m,d)
        return cls(y,m,d).out()  #cls = Tool    Tool(y,m,d)  = cls(y,m,d)

str = "2018-9-12"
Tool.delDate(str)

'''
str = "2018-9-12"
tool = Tool.delDate(str)
tool.out()
'''


'''
str = "2018-9-12"
y,m,d = Tool.delDate(str)
tool = Tool(y,m,d)
tool.out()
'''

'''
str = "2018-9-12"
l = str.split("-")
y = l[0]
m = l[1]
d = l[2]

tool = Tool(y,m,d)
tool.out()
'''   
