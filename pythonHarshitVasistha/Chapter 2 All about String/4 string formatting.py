name = "Roshan"
age = 22
print("Hello " + name + " Your age is " + str(age) ) #ugly syntax

#String formatting
#1.using placeholder {} ----(python 3)

print("Hello {} your age is {}".format(name , age+3))

#2.using        ----> Python 3.6

print(f"Hello {name} your age is {age+2}") #string formatting

#average of 3 numbers
a ,b , c = input("Enter 3 numbers seprated by commas").split(",")
# a,b,c = int(input("Enter 3 numbers seprated by commas").split(","))# type error
#we can't use
a = int(a)
b = int(b)
c = int(c)
print(f"The avg is {(a+b+c)/3}")