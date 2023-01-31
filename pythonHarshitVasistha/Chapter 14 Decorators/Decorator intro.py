'''
for decorators, we need to have full understanding of function
To learn about decorators first we need to learn about first class function/closures
function returning other function is known as closure or first class function

'''

# closure intro

# assigning function into a variable which acts same as function


def square(a):
    return a**2


calling_function = square(8)
print(calling_function)
assigning_function = square # calling_function will act same as square fucntion basically sqaure and calling function points to same location

print(assigning_function(7))
print(assigning_function is calling_function)
print(assigning_function is square)
print(square.__name__)
print(assigning_function.__name__)
print(f"square function points to : {square}")
print("assigning function is as memory location : ",assigning_function)

# how to pass function as an argument
# map , filter , max , sorted and other advanced function takes function as a argument
# now let's make our own functions which takes other function as an argument


def cube(a):
    return a**3


l = [1,2,3,4]
l2 = [1,4,6,8,]
print(map(cube, l))
print(list(map(cube, l)))
print(list(map((lambda a:a**3), l)))
print(list(map((lambda a:a**3), l2)))


# creating our own map function
# my_map(func , iterable) takes
def my_map(key_func , iterbale): # two arguments func and iterable
    '''It takes two argument first is func according to which you want to map the iterable item
    and it return a list of mapped item of iterable
    '''
    new_list = []
    for item in iterbale:
        new_list.append(key_func(item))
    return new_list


def my_map_list_comprehesion(key_func , iterbale): # two arguments func and iterable
    '''It takes two argument first is func according to which you want to map the iterable item
    and it return a list of mapped item of iterable
    '''
    return [key_func(item) for item in iterbale]


print(my_map.__doc__)
print(help(my_map))


def is_even(a):
    return not(a&1)


list1 = list(range(1,11))
print(list1)

print(my_map(is_even,list1))
print(my_map_list_comprehesion(is_even,list1))
print(my_map(lambda a: a&1 , list1))
print(my_map_list_comprehesion(lambda a: a&1 , list1))
print(my_map(lambda a: a**2 , list1))
print(my_map_list_comprehesion(lambda a: a**2 , list1))
print(my_map(lambda a: a**3 , list1))
print(my_map_list_comprehesion(lambda a: a**3 , list1))


# -----------***** function returning function **** --------------
# It is also called CLOSURE or FIRST CLASS FUNCTION

# to return a function by another function
# just write: return func_name without parenthesis
def outer_func():
    def inner_func():
        print("inside inner func")
        return 420
    return inner_func # inner_func whole function  is returned by outer_func()

outer = outer_func() # outer stores the return thing which is inner func hence in
# this above statement is : outer = inner_func()
print(outer)
print(outer()) # similar to inner_func()


def outer_func2(msg):
    def inner_func2():
        print(f"message is : {msg}")
    return inner_func2 # here outer_func2 is returning inner_func2


var = outer_func2("Hey motherfucker ") #
# print(f" is var and inner_func2 are same : {var is inner_func2}") # error
var() # calling inner func


def out():
    def inn():
        print("inside inn")
        return 120
    return inn() # here we are returning whatever inn() function returns

inner = out() # in inner the return thing by inn() function
'''
when out() is called it executed inn func and printed inside inn which return 120 
and then the return 120 is returned by out
'''
print(inner)
# print(inner()) # this will print none


# ------**** Example of Function returning function **** ------------
# define a function which can be used to find any power of natural number n

def to_power(power):
    def calc_power(num):
        return num**power
    return calc_power


print(help(to_power))
print(to_power.__doc__)
cube = to_power(3)
print(cube) # cube is same as calc_power
print(cube(3))
squa = to_power(2)
print(squa)
print(squa(4))









