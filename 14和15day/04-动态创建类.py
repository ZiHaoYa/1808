'''
class Dog():
    pass
'''

#dog = Dog()



def test(arg):
    if arg == 1:
        class Dog():
            pass

        return Dog

    else:
        class Cat():
            pass

        return Cat


Dog = test(1)
dog = Dog()
dog.name = "tom"
print(dog)
print(dog.name)
