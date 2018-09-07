class Car:
    def run(self):
        print("跑")

    def music(self):
        print("听音乐")

bmw = Car()#创建bmw实例或对象
bmw.run()
bmw.music()

bmw.color = "red"#添加属性
bmw.type = "bmwx5"
print(bmw.color)
print(bmw.type)


bc = Car()
bc.run()
bc.music()
bc.color = "white"
bc.type = "bcg"
print(bc.color)
print(bc.type)
