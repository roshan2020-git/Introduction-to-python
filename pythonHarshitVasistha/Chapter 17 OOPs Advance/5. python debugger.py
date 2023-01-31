import pdb  # import pdb (python debugger module ) used for debugging
# any module imported should be written at the top of the program

# what is debugging?
# Debugging is the process of finding and resolving defets or problems within a computer program thta prevent correct operation
# of cmoputer software or a system

# why Debugging?
# 1.) our progrom is not running and causing unexpected error
# 2.) Our program is working fine pbut not working that prevent correct operation


# steps for debugging
# 1.) set trace
# 2.) execute code line by line


'''
in terminal use some commands
l -> to check which line is being execute
n-> to execute  next line
q-> to quit debugging
c -> continue the normal execution  and stop debugging 
'''

pdb.set_trace() # after here whatever the code is written will be executed line by line
# i.e debugging will start after here



name = input("please , enter your name")
age = input("please type your age :")
print(f"Hello {name} and your age is {age}")
age2 = age + 5 # we know error is here cuz it's a very simple code
print(f"{name} and you will be {age2} in next five years")
