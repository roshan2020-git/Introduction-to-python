#declaring more than one varible in single line
name , age  = "Roshan" , 44
print("Hello " + name + " Your age is " + str(age))
x=y=z=1
print(x+y+z)

#two or more input using input()
'''
name = input("Enter your name: ")
print(name)
age = input("Enter your age: ")
print(age)
'''

'''
new_name , new_age  = input("Enter your name and age seperated by spaces ").split() # space is delimiter
#split() by default split the input whenever space is there i.e space is delimiter
print("Your name is " + new_name , " Your age is " ,  new_age)
'''

name1 , name2 = input("Enter two names seperated by commmas: ").split(",") #commaa is delimiter

print(name1, "loves " , name2)



