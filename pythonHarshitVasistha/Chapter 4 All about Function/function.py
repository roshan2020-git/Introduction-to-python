# fucntion in python
# name = "Roshan"
# print(len(name))

'''
# function to add 2 numbers

def add_two_object(a, b):
    return a + b


print(add_two_object("a", "b"))
print(add_two_object(4, 6.0))

obj1 = input("Enter the first object you want to add")
obj2 = input("Enter the second object you want to add")
obj1 = float(obj1)
obj2 = float(obj2)
print(add_two_object(obj1,obj2))
'''


# function to return last char

def last_char(name):
    return name[-1]


print(last_char("Roshan"))


def odd_even(num):
    if num & 1:
        return "odd"
    else:
        return 1


def odd_even2(num):
    if num & 1:
        return "odd"
    return "even"


n = int(input("Enter a number to check it's even or odd :"))
print("odd even" ,odd_even(n))
print(odd_even2(n), end="")
print()


def is_even(num):
    return not (num & 1)


print(is_even(20))


def play_song():
    return "Happy Birthday to you"


def greater(a, b):
    if a > b:
        return a
    return b


print(greater(4, 5))


def greater_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


print(greater_of_three(1, 2, 3))


# function inside function
def greatestOfThree(a, b, c):
    # bigger = greater(a,b)
    # return greater(bigger,c)
    return greater(greater(a, b), c)


print(greatestOfThree(10, 20, 30))


# KISS - keep it simple Stupid

def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("ab"))


# fibonacci series
def fibo(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(a, b, end=" ")
        for i in range(n - 2):
            c = a + b
            print(c, end=" ")
            a = b
            b = c


print("10th term fibo series is ")
fibo(10)


# Default parameters in function
# in function paramatere default paramatere are  to be declared at the end
# defalut argument k baad k sabhi argument bhi deafult value se intiilaised hone chahhiye wrna error aayegi
def user_info(first_name, last_name="unknown", age=None):
    print(f"Your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"Your age is {age}")


user_info("Roshan", "Gupta")
'''
# Variable Scopes
glob_x = 7 # it's a global varibale
def func():
    x = 7 # local variable
    return x
'''


def func2():
    x = x + 7
    print(x)


# can't use varible x bcz it's  scope is inside func 1 so can't be acccessed anywhere else
'''
# print(x)--> error x is not definedglob_x = 7 # it's a global varibale

'''

x = 7  # global varible -- can be accessed anywhere in the program


def func():
    global x  # globally defined variable
    x = x + 6
    return x


def func2():
    global x
    x = x + 7
    print(x)


print(x)  # -->  No error and will print 7
print(func()) # 7 + 6 = 13
print(func2())  # this will print none bcz func2() return type is nothing

#-------*******
