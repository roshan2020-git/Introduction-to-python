'''
tuple is a data Structure
it can store any type of data as list was storing
List was Mutable but Tuple is Immutable
i.e once tuple is created we can't update data inside tuple
'''
ex_tuple = ('one', 'two ', 'three', 1, 2, 3, None, 1, 2, 5)
# we can't append , insert , pop ,remove
# tuple is used we don't need to update the data
# Tuples are faster than list
# methods in tuple
# count , index  , len , slicing
print(tuple)
# ex_tuple[0] = 23 # TypeError: 'tuple' object does not support item assignment
print(ex_tuple.count(1))
print(ex_tuple.index(1))
print(len(ex_tuple))
print(ex_tuple[0:5:2])
print(ex_tuple[::-1])

# --------- **looping in tuple**---------
mixed = tuple(range(1, 10))
print(type(mixed), mixed)
print("Printing tuple item using for loop :")
for item in mixed:
    print(item, end=",")
print()
# tuple with one element
num = (1)
print(type(num))  # <class 'int'> not tuple
num1 = (1,)  # need to put , after first element so that compiler could understand it's tuple
print(type(num1))  # <class 'tuple'>
print(num1)
word = tuple('a')
print(type(word))
print(word)

# tuple without paranthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))
print(guitars)

# tuple unpacking
# needs to declare n variable to unpack tuple of size n
fruit = ('mango', 'Guava', 'Grapes')
f1, f2, f3 = (fruit)  # all these n variable will store the n elemets of tuple
print(f1, f2, f3)

# list inside tuple
# we can perform all the operation related to list on the list  which is present in tuple

list_inside_tuple = (1, 2, 3, ["ram", 2.0, None, False], "hii")
# we have list at index 3
list_inside_tuple[3].append("append")
print(list_inside_tuple)
list_inside_tuple[3].pop(2);
print(list_inside_tuple)

# ---------** function that can be used in tuple**----------
# min(),max() , sum()
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(min(tuple1))
print(max(tuple1))
print(sum(tuple1))

# --------** Function returning 2 values **---------------

# whenever a function return 2 values the values are stored inside a tuple
# we can upack the tuple using two variable to retrieve the data inside tuple

def add_multiply(a,b):
    return a+b , a*b


var = add_multiply(2,3)
print(type(var) , var)
print(var[0],var[1])

added , multiplied = add_multiply(10,20) # tuple unpacking
print(type(added) , added)

# -------------** more about tuple , list , str **-------------
nums = tuple(range(1,11))
print(nums)
# covert tuple into list and string
nums_list = list(nums) # tuple changed to list , original tuple did not change
print(type(nums_list) , nums_list)
print(type(nums) , nums)
nums_str = str(nums) # tuple changed to string
print(type(nums_str) , nums_str)
print(type(nums) , nums)
list_to_str = str(nums_list)
print(type(list_to_str) , list_to_str)


