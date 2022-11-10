# make flexible functions
# * operator
# *args as a normal  parmaeter(when fun is build) of function
'''
using * operator in argument of an function we can give as many paramtere as we want
* operator creates tuple of all parameter and perfoms the task on it
in *args the argument passed should be Hashable in nature
in *args it can take only ordered and hashable datas like list and tuple but not set and dictionary
which are not hasable and also unordered
'''


def total(a, b):
    return a + b


print(total(2, 4))


# what if we need to get total of 100 numbers?
# print(total(1,2,3,4)) # TypeError: total() takes 2 positional arguments but 4 were given

# using * operator or *args
def all_total(
        *args):  # instead of args we can write anything like nums , parametre, roshan ,etc etc but args is recommended to make code readable
    print(args)
    print(type(args))


def aise_hi(*roshan):
    print(roshan)
    print(type(roshan))


all_total(1, 2, 3, 4, 4, 5, 6, 7)
aise_hi(1, 2, 3, 4, 4, 5, 6, 7)


# aise_hi('abc',1,3,{1:2,3:5},(9282,'i you',{1:2,3:5}) ,{'abc',1,[[]]},[1,2,3])

def sum_of_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_of_all(1, 2, 3, 4, 5, 6, ))


# print(sum_of_all('a','b','c','d')) # can't add as total has been itialised with the value 0 which is int and int and sting can't be added

# -------------*** args with normal parameter ***----------------------

def multiply_nums(*args):  # args are option argument i.e if we don't pass arugument during fucntion call it won't throw an error simply a empty tuple will be there
    total = 1
    print(f"passed arguments are :{args}")
    for i in args:
        total *= i
    return total


print(multiply_nums(1, 2, 3, 4, 5))
print(multiply_nums())


def multiply_nums1(num, *args):  # here num is the reuired argument which must be passed during fucntion call
    total = 1
    print(f"num is {num} and passed arguments are :{args}")
    for i in args:
        total *= i
    return total


print(multiply_nums1(2, 3, 4, 5, 6))
print(multiply_nums1(2))
# print(multiply_nums1()) # TypeError -- missing 1 required positional argument : 'num'
# normal parameter must come before *args otherwise it will give error

# -----------{ *args as a argument(when fucntion is called) } -----------
print("args as a argument (argument is the value we pass when we do a fucntion call)")


def multiply_result(*args):
    total = 1
    print(f"args is {args}")
    for i in args:
        total *= i
    return total


num_list = [1, 2, 4]
num_tuple = (1, 2, 3)
num_set = {1, 2, 3}  # can't be unpack cuz it is unordered and unhashable

print(multiply_result(num_list))  # whole list  is as a  single argument
print(multiply_result(*num_list))  # list elements are as arguments
print(multiply_result(num_tuple))  # whole tuple  elements are as arguments
print(multiply_result(*num_tuple))  # tuple elements are as arguments
print("Whole set is passed as a argument ", multiply_result(num_set))  # whole set elements are as arguments
print("set can not be passed bcz it is unhashable ", multiply_result(*num_set))  # set elements are as arguments
