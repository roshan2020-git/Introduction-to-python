# ---------------------******* ENUMERATE FUNCTION *************-------------
#  Enumerate function is used with for loop to track the position of our item
# it is used on iterable data structure
# map object is techinically an iterator i.e we can iterate on map object


# How can we do this without enumerate fucntion

names = ['abc', 'xyz', 'pqr']
'''
print like this 
0 -> abc 
1 ->xyz 
2 -> pqr
'''
print("printing using normal method 1 ")
pos = 0
for name in names:
    print(f" at pos {pos}---> {name} is present ")
    pos += 1
print("printing using normal method 2 ")
# method 2
for i in range(len(names)):
    print(f"at pos {i} ---> {names[i]} is present ")

# using enumerate fucntion
print("printing using enumerate(iterable obj) function ")

for idx, name in enumerate(names):
    print(f"at pos {idx} ---> {name} is present ")

# problem 1 - Define a function that take two arguments
'''
1. list donating strings 
2, String that want to find in your list 
3. function return index of the string in your list and if not present return -1 
'''


def get_index_normal(ls, string):
    return ls.index(string)  # ValueError: 'wxy' is not in list


# index() method return value error if value is not present in the list/tuple/set
# using enumerate func
def get_index_enumerate(ls, string):
    for idx, st in enumerate(ls):
        if st == string:
            return idx
    return -1


ls = ['abc', 'xyz', 'pqr', 'tuv']
string = 'pqr'
print(f"get_index_normal({ls} ,{string}): {get_index_normal(ls, string)}")
print(f"get_index_enumerate({ls, string}): {get_index_enumerate(ls, string)}")
# string = 'wxy'
print(f"get_index_normal({ls, string}): {get_index_normal(ls, string)}")
print(f"get_index_enumerate({ls, string}): {get_index_enumerate(ls, string)}")


# -----------------------*********** MAP FUNCTION/object ***** --------------------
# map is an object
# SYNTAX: map(function name only without () , iterable Data structure)

# given a list return a list of square of number
# method 1: using simple iteration method returning new list
def square_normal(ls):
    op = []
    for num in ls:
        op.append(num ** 2)
    return op


def square_normal_listcomprehesnion(ls):
    return [num ** 2 for num in ls]


# method 2: updating in the same list using
def square_normal2(ls):
    for idx in range(len(ls)):
        ls[idx] = ls[idx] ** 2
    return ls


# method 3 using enumerate function
def square_enumerate(ls):
    op = []
    for ind, val in enumerate(ls):
        op.append(val ** 2)
    return op


# method using lambda function
def square_lambda(ls):
    output = []
    for ele in ls:
        sq = lambda a: a ** 2
        output.append(sq(ele))
    return output


nums = [1, 2, 3, 4]


# using MAP(func , iterbale) function # use this map object when you need to deal with already predefined function like len()
#becuase code becomes short
# function which will be passed in map as an argument
def square(a):
    return a ** 2


square_map = list(map(square, nums))
square_map2 = list(map(lambda a: a ** 2, nums))
print(f"nums list is : {nums}")

print(f"using square_normal(ls): {square_normal(nums)} ")
print(f"updated list is :{nums}")

print(f"using square_normal2(nums) and list will be updated : {square_normal2(nums)}")
print(f"updated list is :{nums}")

print(f"using square_normal_listcomprehesnion(nums): {square_normal_listcomprehesnion(nums)}")
print(f"updated list is :{nums}")

print(f"square_enumerate(nums): {square_enumerate(nums)}")
print(f"updated list is :{nums}")

print(f"square_lambda(nums): {square_lambda(nums)}")
print(f"updated list is :{nums}")

print(f"using map object:", square_map)
print(f"updated list is :{nums}")

print(f"using map object where lambda function as a argument :", square_map2)
print(f"updated list is :{nums}")

# iteration in map
# We can iterate only once in map object
# to run more loop then we need to typecast the map object to other object like list , tuple ,sets
naam =  ['abc', 'xyz', 'pqr']
length = map(len , naam)
print(f" type of map obj is {type(length)} and map is {length}")
# print(le)
print(" 1st iterartion on map ")
for i in length:
    print(i)
    print(type(i))

print(" 2nd iteration on map")
for j in length:
    print(f"trying to print j : {j}")
print("Nothing is printed as we can iterate only once on map \n ")



# ----------------------******** FILTER FUNCTION *****----------------
print("FILTER FUNCTION IN PYTHON ")
def is_even(a):
    return a%2 == 0

numbers1 = [2,3,4,5,2,34,42,12,8,9]

print(filter(is_even,numbers1))
even_nums_filter = filter(is_even,numbers1)
even_nums_tuple = tuple(filter(is_even, numbers1))
even_nums_list= list(filter(is_even, numbers1))
print(set(even_nums_filter) , type(even_nums_filter))
'' \
''

print(even_nums_tuple , type(even_nums_tuple))
print(even_nums_list, type(even_nums_list))

# iteration over filter object
for even in even_nums_filter:
    print(even , type(even))

print("like map object we can iterate on filter object only once but after typecasting filter object to other iterable object we can itereta as many times as we want ")
for even in even_nums_filter:
    print("tyring to iterate on filter obj 2nd time ")
    print(even , type(even))

# filer using lambda experession
odd_nums = list(filter((lambda a:a&1) , numbers1))
print(odd_nums)


# ----------------*** ITERATOR VS ITERABLE *** ------------------
ls_num = [1,2,3,4,]
ls_map = map(lambda a:a**2 , ls_num) # iterator

print(f"map object returns : {ls_map}")
print(f"Looping on ls_num , {type(ls_num)}")
for i in ls_num:
    print(i, end=',')

print(f"looping on map object(note it is not typecast to any list or other: { type(ls_map)}")
for i in ls_map:
    print(i,end=',')

# tuple , list ,set , filter , map ---> all these objects are ITERABLE
# Execution of for loop
'''
1. calls iter function which converts iterables into iterator
iter(ls_num) ---> iterator of type(ls_num) object
2. next funtion is called into this iter 
next(iter(numbers))

'''

print("Execution of for loop : ")
num_iter = iter(ls_num)
print(num_iter , type(num_iter))
print(next(num_iter) , type(next(num_iter)))
# print(next(num_iter) , type(next(num_iter)))
# print(next(num_iter) , type(next(num_iter)))
# print(next(num_iter) , type(next(num_iter)))
# print(next(num_iter) , type(next(num_iter)))
# print(next(num_iter) , type(next(num_iter)))

'''
filter and map objects return an iterator so we can use next func i.e  next(iterator) to print 
the value it is pointing and then current itetrator will point to next item to the current iterable object
'''
# if we pass an iterable to next() as an argument then we will get TypeError in it
# print(next(ls_num)) # TypeError: 'list' object is not an iterator


# -----------------*** ZIP function *** --------------

# zip fucntion is used to zip


user_id = ['user1' , 'user2' , 'user3']
user_name = ['roshan' , 'rohan']

# after zipping -> ('user1' , 'roshan' , 'user2' , 'rohan')
# size of zip obj will be the min size of among passed arguments

zip_iterator = zip(user_id , user_name) # returns a zip object which contains tuple of crrosspondecne elemet of passed arguments
print(zip_iterator)
for i in zip_iterator:
    print(i , type(i))

# here is a catch after running the for loop zip_iterator is passing to none cuz we have travelled the whole zip object once
# now if we try to convert it into list we gonna get an empty list
zip_iterator = list(zip_iterator)
print(zip_iterator, type(zip_iterator))

# these kinds of zip object can be converted to dictionary cuz each tuple has two value which is similar to dictionary
print(dict(zip(user_id,user_name)))

# we can pass as many argument as we want in zip func
user_salary = [1000,10281,91382,1010238]

print(zip(user_id,user_name,user_salary))
print(list(zip(user_id,user_name,user_salary)))
print(tuple(zip(user_id,user_name,user_salary)))
print(set(zip(user_id,user_name,user_salary)))
# print(dict(zip(user_id,user_name,user_salary))) # ValueError: dictionary update sequence element #0 has length 3; 2 is required

#  ------***** more about zip ********------------
# * operator with zip
l1 = [1,3,5,7]
l2 = [2,4,6,8]
l3 = list(zip(l1,l2)) # l3 = [(1,2),(3,4),(5,6),(7,8)]
print(l3)
# unzip the zip object
print(list(zip(*l3))) # [(1,3,4,7) ,(2,4,6,8)]
new_l1 ,new_l2 = list(zip(*l3))
print(new_l1,new_l2)
print(list(new_l1),list(new_l2))

new_list = []
for pair in zip(l1,l2):
    print(pair)
    new_list.append(max(pair))
print(new_list)


