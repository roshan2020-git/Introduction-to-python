# lambda Expression (anonymous fucntion)
# Lambda function is declared in one line and has no name of it
# syntax: lambdaKeyword arguments : return Statement
# lambda function are used with built in function like map , reduce , filter
def add(a, b):
    return a + b


add2 = lambda a, b: a + b  # we can assign the lambda function in a varibale but we genrally need not to do it
# Here add2 can be treated as a name of the lambda function i.e wherever we need this lamda fucntion we can use it by calling add2(a,b)
print(f"priniting sum using lambda expression : {add2(1, 2)}")
print(f"priniting sum using add(a,b) function  :{add(2, 3)}")


def mul(a, b):
    return a * b


multiply = lambda a, b: a * b
print(f"printing multiplication  using add(a,b) function  :{mul(2, 3)}")
print(f"printing multiplication using lambda expression : {multiply(1, 2)}")

# lambda as an anonymous function
print(add)  # return address of fuc add  i.e <function add at 0x000002134C279090>
# returned address will be changing everytime when we execute cuz at each execution different memory allocated to the
# function
print("Trying to print address of lambda function add2 and mul  ")
print(add2)  # <function <lambda> at 0x000002429C759120>

print(multiply)  # <function <lambda> at 0x000002429C759240>


# lambda expression practice
# check even function using lambda expression
def is_even(a):
    return not (a & 1)


is_even2 = lambda a: not (a & 1)

print(f"printing using normal function -> is_even(3):{is_even(3)}")
print(f"printing using lambda expression -> is_even2(3):{is_even2(3)}")


# printing last char using lmabda expression
def last_char(s):
    return s[-1]


last_char_lambda = lambda string: string[-1]

last_char_lambda_2 = lambda string: string[-1] # see the correction recommended by PyCharm IDE

# any: (string: Any) -> Any = lambda string: string[-1]

print(f"printing using normal function -> last_char('roshan'):{last_char('roshan')}")
print(f"printing using lambda expression -> last_char_lambda('roshan'):{last_char('roshan')}")


# lambda Expression with if else
# synxtax:  lambdaKeyword argument : returnStamentOfif  if  (condition) else returnStatementOfELse
def is_greater_than_5(s):
    return len(s)>=5


is_greater_than_5_lambda = lambda s:True if len(s)>5 else False
is_greater_than_5_lambda2 = lambda s: len(s)>=5

print(is_greater_than_5('roshan'))
print(is_greater_than_5_lambda('roshan'))
print(is_greater_than_5_lambda2('roshan'))