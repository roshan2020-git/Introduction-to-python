print("Hello Wor'ld") #can't use double quote inside
#print("roshan"Gupta" ") #invalid syntax
print('hello Wo"rld') #can't use single quote
'''
Triple qoute can be used as multiline comment and can also be used inside print function
see the below example
'''
print(''' print"" Hello Roshan's Kumar ji Gupta''')
print(''' Hii There ,
How are you doing?
I am doing fine.
What about Yourself?
"I'm fine"
''')
'''
this is multilie comnt

'''
#ESCAPE SEQUENCE CHARACTER -- \" , \' , \\ , \n , \t , \b



print("Hii \"Roshan \" ")
print('I\'m Roshan\bGupta.  ')
print("this is backslash\\")#use \\ to print \
print("this is double backslash\\\\") #use \\\\ to print \\


#Escape character as normal text

#output: Line A \n Line B

print("Line A \\n Line B")
print("Line A \\t line B")

# output:\" \'
print("\\\" , \\\' ")# \' -> ' , \\->\ => \\\'

#Exercise


print("this is \\\\ double backslash")
print('''this is \\\\ backslash''')
print(r"this is \\ backslash") # RAW string in python -> print(r"sring")
print(r"this is /\/\/\/\ mountain")
print("this is /\/\/\/\ mountain")
print(r"\\ , \" , \' , \n , \t")
print("this is / forward slash")
print("this is /\\/\\/\\/\\ mountain")
print("I'm \t awesome")
print("\\\" , \\n , \\t , \\\'")
print("emoji \U0001F602")
print(2^4)
print(1/2)
print(1//2)
print(round(3/4))
print(2**4**2)
print(2**0.5)
print(round(2**0.5 , 4))
print(3%2)
print()
print("2 to tghe power 68 is " , str(2**68))

#Precedence rule
'''
parentheses ---> Highest
Exponent --> Right to left
*,/,//,% --> left to Right
+,- --> left to right 

'''

print((2+3)*5%10) # 2+3 = 5 * 5 = 25%10 = 5
print((2+3)*5%10//2%5)

#exponent -- Associativity RIGHT to LEFT
print(2**4)#2 to power 4 = 8
print(2**4**3) # 4 to power 3 = 64 then 2 to the power 64
print(2**64)

#varibale in python
num1 = 2
print(num1)
num1 = "Roshan" #dynamic nature of varible -- changing it's data type during run time
print(num1)
#Rules for naming of varibale
'''
1. varible name can not start with number 
2. varible name first letter can be alphabet or _
3. varible name can't start and can't have special char like % , & , * etc

'''
#Naming Convention for varible
'''
1. separate variable names using underscore
eg. user_one_name = "Roshan" #snake case writing

2. Camel Case writing of Variable name
eg. userOneName = "Gupta"

'''