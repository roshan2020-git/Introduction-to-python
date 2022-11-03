'''
syntax
if condition:
    code if contion is true then this code will execute
'''
#------------------*****************----------------
'''
age = int(input("Enter your age"))
if (age>=14): # if age>=14 this is also correct
    print("You are above 14")
    print("some codes are written inside this if block")
else:
    print("You are below 14")
    
'''
#pass keyword --  it is used when we don't want to write any code in if block
x = 120
if x>18:
    pass
else:
    print("not in pass")
    
    


#-------------------------**********************--------------

#Exercise - guessing number
'''
jackpot = 69
num = int(input("Guess a number between 1 to 100 "))
if(num==jackpot):
    print("YOU WIN!!!")
elif num<jackpot:
    print("Guess low number" , end="")#cursor won't go to new line bcz we said end=""
else:
    print("Guessed to high number")

#check two conditions at same time
# and , or
name = "abc"
age = 19
if name=='abc' and age == 19:
    print("condition true")
else:
    print("condition false")


name = "abc"
age = 19
if name=='abc' or age == 69:
    print("condition true")
else:
    print("condition false")

'''

#--------------------------***************--------------------

#Exercise
'''
username , age = input("Enter comma separarted  your name and age ").split(",")
age = int(age)
if ((username[0]=='a' or username[0]=='A') and age>10):
    print("You can watch coco Movie")
else:
    print("sorry , you can not watch coco")
'''
#---------------**********-------------
'''
#if elif and else
age1 = int(input("Enter your age "))

if age1<=0:
    print("Inavlid age input")
#if else elif ladder
if 0<age1<=3:
     print("Ticket price: Free")
elif 3<age1<=10:
    print("Ticket Price: 150")
elif 10<age1<=60:
    print("Ticket price:250")
else:
    print("Ticket Price: 200")

'''
'''
#in keyword
# name = "Roshan"
name,ch = input("Enter commma separetd name and any character ").split(",")
if ch in name:
    print(f"{ch} is present in {name} ")
else:
    print(f"{ch} is not present in {name} ")

'''
#Check Empty or not
Name = ""
# Name = "abc"
if Name: # true when string/object is not empty
    print("string is not empty")
else:
    print("string is empty")
