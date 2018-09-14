try:
    number = int(input("请输入一个"))
except Exception as ret:
    print("输入有误")
    print(ret)


number = input("请输入一个")
if number.isdigit():
    print("出数字")
    number = int(number)
else:
    print("输入有误")
