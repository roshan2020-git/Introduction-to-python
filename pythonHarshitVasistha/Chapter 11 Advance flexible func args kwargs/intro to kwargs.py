# ** operator or kwargs or key word argument

# kwargs as a parameter
# kwargs takes input as a dictionary
# args take input as a tuple

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))


func(first_name='Roshan', last_name='Gupta')


def func2(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")


func2(first_name='Roshan', last_name='Gupta')

print("kwargs as a argument when func is called ")
# kwargs as
#
#
#
# an argument(when function is called)
d = {'name': 'roshan', 'age': 22, 'state': 'U.P'}
func(**d)
func2(**d)

# function with all type of parameters
# PADK ---> parameters , *args ,  default , **kwargs

def para_func(name ='unknown' , age = 24):
    print(name , age)

para_func()
para_func('roshan')
para_func(24)
print('roshan',22)


def order_para_fun(normal_para , *args, deault_para ='unknown',**kwargs):
    print(f"Normal para is :{normal_para}")
    print(f"args is {args}")
    print(f"deault_para is {deault_para}")
    print(f"kwargs is {kwargs}")

order_para_fun('roshan' , *[1,2,3] , a=1,b=2)
order_para_fun('gupta' , 1,2,3 , a=1,b=2)