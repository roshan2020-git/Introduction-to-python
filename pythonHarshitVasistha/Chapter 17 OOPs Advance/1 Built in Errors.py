# chapter 17
# built in errors
# exception handling , how to handle them
# raise your own errors , debugging etc


# Syntax error -- wrong syntax
# indentation error - proper indenataion is not given
# name error - when we try to access things which are not declared/defined
# Type Error - when we try to perform wrong  operation with wrong operands
# index error - trying to access invalid indices
# value error -  st  = 'abc' print(int(st))  -- value given to int is wrong
# attribute error -
# key error - key not present in dict/ set


# RAISE ERROR

def add(a,b):
    return a+b

def add_int_only(a,b):
    if (type(a) is int) and (type(b) is int):
        return a +b
    # return "OOPS you entered wrong data type "
    raise TypeError('OOPs you are passing wrong data type in function ')

# why we are not returning string only ?
# if we have to store data somewhere and if wrong input is fed then we are going to store string output
# which we don't want to use it . SO Raising error will be best solution

# Error Raising Example 1
# NotImplementedError
# abstract method - in java abstract method is same as here as eg we are using NotImplemetedErro


class Animal:
    def __init__(self , name ):
        self.name = name
    # abstract method
    def sound(self):
        # return "This is an animal sound "
        raise NotImplementedError('You have to define sound method in each subclass of animal class')
class Dog(Animal):
    def __init(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Cat meous"

'''
each subclass of animal class will have the sound so if anyone doen't have then it will search for the parent clas
so in parent class we will have to make a sound method which will raise an error of not implemented
cuz every animal has different sound 
'''


# Error raising Example 2
class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobiles(self, new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise  TypeError('new Mobile should be object of Mobile Class')

onePlus = Mobile('one plus 6t')

samsung = 'Samsung Galaxy s12'

mobstore = MobileStore()
print(mobstore.mobiles)
# mobstore.add(samsung) # AttributeError: 'MobileStore' object has no attribute 'add'
print(mobstore) # here 'Samsung Galaxy s12' will be added in the list
# but we want that only mobile class object are to be added in the list

mobo_list = mobstore.add_mobiles(onePlus)
print(mobo_list[0].name)


