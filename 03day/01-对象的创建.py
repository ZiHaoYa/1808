class Dog():
    

    def sleep(self):
        print("睡觉")
    
    def eat(self):
        print("吃饭")

    def introduce(self):
        print("名字是%s 年龄是%d"%(self.name,self.age))

hsq = Dog()#创建一个实例
hsq.sleep()
hsq.eat()

hsq.name = "二哈"
hsq.age = 10

hsq.introduce()


