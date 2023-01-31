'''
Decorators are used to enhance the functionality of other function

'''

def func1():
    print('this is func1')


def func2():
    print("this is func2")

func1()
func2()

# we want that the func1 and func2 remains same but both or either prints extra line
# for eg when we call any func1 or func2 it also prints " this is awesome"

def decorater_func(any_func):
    def wrapper_func(): # which adds functionality to any_func
        # adding functionality
        print("this is awesome")
        any_func() # calling any_func
    return wrapper_func

var1 = decorater_func(func1) # passing reference of function only cuz we are not using () otherwise func call will happen not func passing
# now var1 is same as wraper_func i.e var is func which has same code as wrapper func
print(var1 is func1)
'''

def var1():
        print("this is awesome")
        func1 # calling fun1
'''
var1() # caling wrapper fun which first print this is awesome adn the calls func1()



var2 = decorater_func(func2)
var2() # same as calling wrapper function which first prints this is awesome and then calls passed any_func here it is func2


# syntatic sugar
'''
before definning any func if we use @decorator_function_name 
this we autoamtically add the decoration function feature to it and whenever we call the defining func
it wiil autamitcially executed with functionality 

'''
def deco_fun(any_fun):
        def wrapper_func():
            print("We are inside decorator func")
            any_fun()
        return wrapper_func


@deco_fun
def fun1():
    print(" we are in fun1")


@deco_fun
def fun2():
    print(" we are in fun2 ")

@deco_fun
def fun3(a):
    print(f"The argument is : {a}")

fun1()
fun2()
print(f"fun1() with modified : {fun1()}") # first fun1() (modified )will be called and whatever it has to execute will will exeture and then
# whatever fun1 will return will be replaced in place of {fun1()} in print
print(f"fun2() with modified :{fun2()} ") # first fun12() (modified )will be called and whatever it has to execute will will exeture and then
# whatever fun2 will return will be replaced in place of {fun1()} in print


# Decorator function part 2 :
# there were some error. what if we pass some argument in func3

fun3(7)
