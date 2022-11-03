'''
#this code will add two string which are taken input from the user 
num1 = input("Enter num 1: ")# string as input
num2 = input("Enter num 2:" )# string as input
total = num1 + num2 #concatenation of string
print(total)
'''

#------------------------*********-----------------------------


'''
#correct code to add two numbers
first = int(input("Enter first number "))
second = int(input("enter second number "))
print(first + second)# addition of two numbers
print("The sum is " + str(first + second))#need to typecast to  string as we can't add string and int
'''
# int() , float() , str() , bool() --- typecast function
number1 = str(4)
print(type(4))
print(type(number1))
print(number1)
number2 = float("44")
print(type("44"))
print((type(number2)))
print(number2)
number3 = int("33")
print(type("33"))
print(type(number3))