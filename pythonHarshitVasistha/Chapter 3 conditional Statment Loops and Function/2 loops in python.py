
#---------------****** WHILE LOOP IN PYTHON *******-----------------

'''
# while loop
i = 1
while i <= 10:
    print(f"Hello world {i}")
    i += 1 # i = i+1 but i++ will gave an error cuz int is immutable so i++ won't be valid
# i+=1 returns a different object
# sum of n natural number
total = 0
i = 1
while i <= 10:
    total += i;
    i += 1
print(total)

'''

# Exercise
'''
#1. sum of n natural number 
n = int(input("Enter the number upto which you want to get sum : "))
i =sum=0
while i <= n:
    sum += i
    i += 1 # int is immutale hence this statment return an onother object of type int whose value is i+1
print(f"sum of first {n} natural number is {sum}")

'''


'''
#2 - digit sum of number
number = input("Enter a number containig more than one digit : ")
dgSum = 0
total_digit = len(number)
i = 0
while i < total_digit:
    dgSum += int(number[i])
    i += 1
print(f"The digit sum of {number} is {dgSum}")

'''

'''
#3 count occurence of any char in a string
name = input("Please , Enter Your name : ")
i = 0
is_char_already_count = ""
while i < len(name):
    if name[i] not in is_char_already_count:
        print(f"{name[i]} : {name.count(name[i])}")
        is_char_already_count += name[i]
    i += 1

#Infinite loop in python
#while(1) , while(True)

'''

#-----------------------FOR LOOP in PYTHON ----------------------

'''
# FOR LOOP WITH RANGE FUNCTION
for i in range(10): # i ranges from 0 to 10-1=9
    print(f"Hello World i - : {i}")
for freq in range(2,11): # freq ranges from 2 to 11-1=10
    print(f"Hello Roshan freq -: {freq}")

'''

'''
#sum of n natural number using for loop
n = int(input("Enter nth natural number of your choice : "))
total = 0
for curr_num in range(1,n+1):
    total += curr_num
print(f"The sum of {n} natural number is {total}")

#sum of digit of natural number

num = input("Enter the number whose digit sum you want to find :  ")
digit_sum = 0
#method 1
for digit in num:
    digit_sum += int(digit)
print(f"The sum of digit of natural number {num} is {digit_sum}")

#method2
digit_sum2 = 0
for i in range(len(num)):
    digit_sum2 += int(num[i])
print(f"The sum of digit of natural number using method 2 {num} is {digit_sum2}")

'''


'''


# count occurrences of each unique characters in a string
name = input("Enter your name :")
is_present = ""
for ch in name:
    if ch not in is_present:
        print(f"{ch} : {name.count(ch)}")
        is_present += ch

print("for loop ended")


'''
'''
#BREAK AND CONTINUE KEYWROD

for i in range(1,11):
    if i == 5:
        break
    print( i ,end=" " )
print()
for i in range(1, 11):
    if i == 5:
        continue
    print(i ,end="")
'''


'''
#step argument in range
for i in range(1, 100, 2): # start = 1 , end = 99 , step = 2
    print(i, end=" ") #all odd number are printed
print()
print("all even number from 0 to 99 are :")
for even in range(0, 100, 2):
    print(even, end=",")
print()
for neg in range(0,-100,-1):
    print(neg,end=",")
    
    
'''

#------------*****For Loop in String****** -----------------

name = "Roshan"
for i in range(len(name)): # here i ranges from index 0 to len-1
    print(name[i],end="")

print("\nfor each loop in Python :")
for i in name: # Here i ranges from name[0] to name[n-1] i.e for every char of string
    print(i,end="")
print()
#digit sum code using for each loop
n = "1838381"
total = 0
for digit in n:
    total += int(digit)
print(total)