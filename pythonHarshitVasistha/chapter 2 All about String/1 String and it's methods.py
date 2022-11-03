
first_name = "Roshan"
last_name = "Gupta"
full_name = first_name + " " + last_name
print(full_name)

# print(first_name+3) #type error -- string can't concatenate with number
print(full_name + str(3))
print(full_name + "3")

print(first_name*3)# first_name added 3 times with itself

#user input
# input() -- return string
name = input("Enter your name")
print(type(name))
print("Your Name is " , name)
print("Your Name is " + name)

age = input("Enter your age")
print(type(age))
print(age)
age = int(age)
print(type(age))
print(age)


# first__Name  = input()
# last__name = input()
# print(first__Name+last__name)
