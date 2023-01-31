'''
make a function 'divide'
divide(a,b)
print(divide(4,2))  --> 2
print(divide(4,0)) --> ZeroDivisionError
print(divide('4' , 2)) # please input number only
'''


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as Terr:
        print(Terr)
        print("Numbers should be int or float ")
    except:
        print('Unexcepted Error!!!')
    else:
        return a/b


print(divide(2,3))
print(divide(2,0))
print(divide(2,'2'))
