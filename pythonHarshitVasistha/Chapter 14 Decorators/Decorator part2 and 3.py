
# handle function with arguments

def decorator_function(any_function):
    def wrapper_function(*args , **kwargs):
        print(" this is awesome function")
       # return any_function(*args , **kwargs) # return is must to write
    return wrapper_function


@decorator_function
def fun(a):
    print(f" this is function with argument {a}")

@decorator_function
def add(a,b):
    return a+b

print(add(2,3))