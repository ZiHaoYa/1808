import random
class addCount():

    l = []#装数字
    
    @classmethod
    def add(cls):
        while True:
            count = random.randint(1,100)
            if count not in cls.l:
                cls.l.append(count)
            
            if len(cls.l) == 10:
                break
        return cls.l


l = addCount.add()        
print(l)
