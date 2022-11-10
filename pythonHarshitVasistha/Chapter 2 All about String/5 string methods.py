name = "Roshan Gupta"
print(len(name)) #function
#string methods in python

#1. lower() -> return a string of lowercase letters only , doen't change the actual string

print(name.lower())
print(name)#signifies the string doen't altered
new_name = name.lower() # storing the lowercase returned string by lower() method
print(new_name)
print(name)#signifies the string doen't altered

# 2.upper() method -- same as lower it return uppercased strings i.e all letters are uppercased
#It also doesn't alter the original string
print(name.upper())
print(name)
Upper_case_name = name.upper()
print(Upper_case_name)
print(name)

#3. title() - Uppercaesd the first letter of every word of the given string and rest convereted to lowercase
book = "thE subTLe arT of nOt giving fuCk"
print(book.title())
print(book)
#4. count(string) -- return the no of occurnces of particular letter
#this method is case sensitive
print(book.count('i'))
print(book.count("arT"))
print(book.count("the"))

#Exericise
'''
yourname , char = input("Enter your name and charcter of your choice : i/p seperated by commas ").split(",")

print(f"your name length is {len(yourname)} and the count of input char is {yourname.lower().count(char.lower())}")

'''
#strip method
myname = "    Ros    han   "
dots = "............"
print(myname + dots)
print(myname.lstrip() + dots)
print(myname.rstrip() + dots)
print(myname.strip() + dots)
print(myname)
print(myname.replace(" " , "") + dots)
print(myname)

'''
yourname , char = input("Enter your name and charcter of your choice : i/p seperated by commas ").split(",")

print(f"your name length is {len(yourname)} and the count of input char is {yourname.strip().lower().count(char.().lower())}")

'''

#replace() and find() methods

string  = " is  she is a beautiful and she is good singer "
print(string.replace("is" , " are")) # all is will be replaced
print(string.replace("is" , "are" , 1)) # only one is will be replaced
print(string.replace("is" , "are" , 1000)) # 1000 is will be replaced

print(string.find("is"))#first occurence
print(string.find("is" , 3)) #first occurence starting from index 3

is_pos1 = string.find("is")
print(is_pos1)
is_pos2 = string.find("is" , is_pos1+1)
print(is_pos2)

# center method
is_name = "Roshan"
print(is_name.center(len(is_name) + 4 , '#'))# add first in left then right and repeats
print(is_name.center(len(is_name) + 5 , '#'))
print(is_name.center(len(is_name) + 1 , '#'))

user_name = input("Enter your name ")
print(user_name.center(len(user_name) + 4 , "*"))

#string are IMMUTABLE i.e
your_string = "String"
# your_string[0] = 'P' #TypeError: 'str' object does not support item assignment4
new_string = your_string.replace('S' , 'P' , 1)#it won't change our original string but this method will return the string which will we get after applying this method
print(your_string)
print(new_string)
#

#assignment operator
paper = "india"
print(paper)
paper = "India today"
paper+=" news"
# we can change the value stored in a varible anytime but can't altered the string value i.e method can change our original string and we also can't chnage char of string
print(paper)