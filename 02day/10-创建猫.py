class Cat():

    def sleep(self):
        print("睡")

    def eat(self):
        print("吃")

    def introduce(self):#谁调用这个方法，self就指对象什么
        print("我叫%s,颜色是%s"%(self.name,self.color))

tom = Cat()
tom.eat()
tom.sleep()
tom.name = "tom"
tom.color = "blue"
tom.introduce()

jfm = Cat()
jfm.eat()
jfm.sleep()
jfm.name = "加菲猫"
jfm.color = "yellow"
jfm.introduce()


