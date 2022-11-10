# define a func which takes any no of lists
# return a list which contains avg of each list elemets
# [1,2,3] [4,5,6] [7,8,9] --->input
# o/p  = [(1+4+7)/3 , (2+4+8)/3 ,(7+8+9)/3]
# doing same for two list only
def avg_2_list(l1,l2):
    avg =[]
    for pair in zip(l1,l2):
        avg.append(sum(pair)/len(pair))
    return avg


print(avg_2_list([1,2,3] ,[4,5,6]))


def avg_list(*args): # args take element as a input in tuple hence *args to unpack
    return [sum(pair)/len(pair) for pair in zip(*args)] # unpack tuple to element


print(avg_list([1,2,3] ,[4,5,6] ,[7,8,9]))

avg_list_lambda = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(avg_list_lambda([1,2,3] ,[4,5,6] ,[7,8,9],[4,4,4]))

#----------********** any , all function ****--------

list1 = [2,4,6,8,10]
list2 = [1,2,3,4,5,6]
# check if all the elements in list are even
is_even_list1 = [not(num&1) for num in list1]
is_even_list2 = [not(num&1) for num in list2]
print(is_even_list1)
print(is_even_list2)
# all function : all(iterable) - returns true if every/all item in iterable is true else return false
print(all(is_even_list1))
print(all(not(num&1) for num in list2))
print(all(is_even_list2))
print(all(['roshan' , 1, 2,[['1',True]]])) # true because every item is not zero and not False/None
print(all(['roshan' , 1, 2,None,[['1',True]]])) # None
print(all(['roshan' , 1, 2,None,[['1',False]]]))
print(all(['roshan' , '', 2,None,[['1',False]]]))
print(bool(None))

# ---------------*** any() ** -----------
# any(iterable) -- if any of the item in iterable is true return true
print(any(is_even_list2))

# practice of any all
def all_Sum(*args):
    # args = ()
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total += i
        return total
    else:
        return "Wrong data input "



# what if we pass data other than int or float , we can;t add str and int
# to avoid this we will be checking if all the arguements are int or float then proccede
# otherwise retunrn wrong input

print(all_Sum(1,2,3,4,5,18.92))
print(all_Sum(1,2,3,4,5,'roshan'))


# --------- **** min() and max() **** --------------
nums = [1,2,4,5,7]
print(max(nums))
print(min(nums))

names = ['roshan' ,'kumar' ,'gupta' ,'up' , 'ballia']
print(max(names)) # lexographically largest string
print(min(names)) # lexographically smallest string

def func(item):
    return len(item)
#max(iterable , key ) # key determines the way we need to find the max in iterable, whatever func is assigned to key it will
# perform on each item of iterbale and then after return max op performing post function operations
print(f"printing max length of item in using normal defined func by me  as key {names} : {max(names, key = func)}")
print(f"printing max length of item in suing lambda func as key  {names} : {max(names, key = lambda item: len(item))}")

student1 = {
    'harshit':{'score':90 , 'age':24},
    'mohit':{'score': 75 , 'age':19},
    'rohit': {'score':76 , 'age':23}
}
print(max(student1 , key = lambda item: student1[item]['score']))

student2 = [
    {'name':'harshit' ,'score':90 ,'age':22},
    {'name':'mohit' , 'score':40 , 'age':23},
    {'name':'rohit' , 'score':70 , 'age':24}
]

# print max on the basis of socre
# max function perform operation according to the key or the func we pass and returns the max elements from the given iterable
# so here max fucn will return a dictionary which is elem of and which will have max socre among them
print("hey")
# print(max(student2 , key = lambda  item:student2[item]['score'])) # eroor in it
print(max(student2 , key = lambda item: item.get('score'))) # here max will return the 2nd dictionary which has max socre
print(max(student2 , key = lambda item: item.get('score'))['name']) # here max will return the 2nd dictionary name  which has max socre
print(max(student2 , key = lambda item: item.get('age'))['name']) # here max will return the 2nd dictionary name  which has max socre


# ---------------**** sorted() function *****------------
'''
1. sorted(iterbale , key) function sorts the given iterbale according to key/func/comparator passed
2. it returns a list of sorted Op
3. it doesn't alter the original iterable i.e original iterbale remains same as it is 
'''
fruits_list = ['grapes' , 'mango' , 'apple']
print(fruits_list)
fruits_list.sort() # sorts the fruits lexographically increasing order
print(fruits_list)
fruits_tuple = ('grapes' , 'mango' , 'apple')
fruits_sets = {'grapes' , 'mango' , 'apple'}
# fruits_tuple.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# print(fruits_tuple) # AttributeError: 'tuple' object has no attribute 'sort'
# sort() doesn't work on tuple
# we can use sorted function to sort tuple
# sorted fucn return list of sorted item but don't change the original as tuple are immutable
# sorted(iterable , reverse = T/F)
fruits_list.append('guava')
print(fruits_list)
new_fruit_list_sorted = sorted(fruits_list)
print(fruits_list) # remained unchanges as sorted() return new list of sorted item and passed iterable remians uncahnged
print(new_fruit_list_sorted , type(new_fruit_list_sorted))

new_fruit_tuple = sorted(fruits_tuple)
print(fruits_tuple , type(fruits_tuple))
print(new_fruit_tuple,type(new_fruit_tuple))
new_fruit_sets = sorted(fruits_sets)
print(fruits_sets, type(fruits_sets))
print(new_fruit_sets , type(new_fruit_sets))

guitars = [
    {'model':'yamaha f310' , 'price': 84000 },
    {'model': 'faith naptune' , 'price': 50000} ,
    {'model': 'taylor 814ce' , 'price':450000}
]

# sort according to price
# sorted func will return list of items of iterable according to the definition of key
print(sorted(guitars , key = lambda d:d['price'])) # we can also use d.get('price'))


# we can also store the above sorted list in a variable

soerted_guitar_reverse_price = sorted(guitars , key = lambda d:d['price'] , reverse=True) # we can also use d.get('price'))
print(soerted_guitar_reverse_price)
print(guitars)


# --------****** More About Function ****** ---------
# what are doc strings
# Ans- Doc string shows us the details about the function
# how to write docstring
# Ans - we can write doc string inside the function using ''' doc string msg'''
# or we can use " doc string msg" but choose any one at a time
# how to see docstring
#Ans - to see doc string msg use   func_name.__doc__
# what is help function
#ans - help(func)

def add(a,b):
    # ''' return sum of 2 items which can be added '''
    " we can also use \"\" to write doc string but use only one of these at a time  "
    return a+b
print(add(3,4))
print(f"Doc string of add() is : {add.__doc__}")
print(f"help(add) is : {help(add)}")

print(f"Doc string of len() is : {len.__doc__}")
print(f"help(len) is : {help(len)}")
print(f"Doc string of max() is :{max.__doc__}")
print(f"help(max) is : {help(max)}")
print("trying to print help(max) without using f string ")
print(help(max))
print(f"Doc string of sum is : {sum.__doc__}")
print(f"help(sum) is : {help(sum)}")
print("trying to print help(sum)")
print(help(sum))

