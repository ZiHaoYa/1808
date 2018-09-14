#coding=utf-8
try:
    #print(b)
    #open("1.txt","r")
    1/0
    #print("老王")
except (NameError,FileNotFoundError):#指定异常捕获
    print("捕获指定异常")
except Exception as ret:#捕获任何异常 ret具体异常信息
    print("捕获任何异常")
    print(ret)
else:
    print("没有任何异常走的逻辑")
finally:
    print("不管有没有异常都会走")

'''
不是所有的代码都需要加上异常
可能会出现一次才加上捕获

'''

number = int(input("请选择功能"))

