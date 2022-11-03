'''
List is a data structure
List is a ordered collection of items with 0 based indexing
List can store any mixture of item like int , float , string
List is MUTABLE in nature
The list is a data type that is **MUTABLE**. Once a list has been created:
Elements can be modified. Individual values can be replaced.
'''

numbers = [1, 2, 3, 4]
print(numbers)
print(numbers[1])  # accessing elements of list
print(numbers[-1])
print(numbers[::-1])
print(numbers[0:2])
print(numbers[0:4:2])
numbers[1] = "two" #list is mutable hence it can be modified without any error
print(numbers)
word = ["word1", "word2"]
print(word)

mixed = [1, 2, 3, "Roshan", 3.282, True, None]
print(mixed)
print(mixed[::-1])
mixed[1] = "two"
print(mixed)
mixed[1:] = "two" # in mixed the element before index 1 will remain as it is and after that each elemnt will be removed and each char of "two" will be the new item of list
print(mixed)
mixed[1:] = ["Three" , "four" , "five" , False , 27.928 , None]
print(mixed)

# Methods on list in python
# add item to list
# 1. list.append() -- add at the end of list
fruits = ["apple" , "Guava" , "grapes"]
print(fruits)
fruits.append("Mango")
fruits.append(1)
fruits.append(None)
fruits.append(True)
print(fruits)

# insert method -- list.insert(idx , obj) # insert the object at specified idx and rest of the item are shifted
# No deletion or updation of item at idx occur.
# item from idx are right shift by one position and the inserted obj ocuupied that palce
# if idx is out of bound then the item will be inserted at the end of lsits
car = ["audi" ,"indigo" , "Bolero" , "scorpio"]
print(car , len(car))
car.insert(1,"Tata Hyundai")
print(car , len(car))
car.insert(3 , ["apple" , "Guava" , "grapes"]) # this whole list will be treated as only one Item
print(car , len(car))
# car.insert(21,"Bugati")
# print(car)
print(car[3])
print(car[3][0])
print(car[3][1])
print(car[3][2])
print(car[3][::])
print(car[3][::-1])


# conactenate two list -- using + operator we can do it
list1 = ["a" , "b" , 1, 2 , None, [1,2,3]]
list2 = ["Roshan" , "1928" , "True" , False]
print(list2+list1)

# extend method list.extend(list2) --  each element of list2 are added at the end of list1 and this method return None
f1 = ["mango" , "guava"]
f2 = ["grapses" , "kaju katli"]
print("start" ,f1.extend(f2))
print("start1",f1)
f2.extend(f1)
print("f2 is" ,f2)

print("f1.append(f2) returns :" , f1.append(f2))
print(f1) # whole f2 will be added in the end of f1
print("f2  is : " ,f1[len(f1) -1]) # this will print f2


#-------Methods to delete data from list---------
movie = [" Iron man" , "Avenger " , "Hulk" , "Mrs. Marvel"]
 # list.pop(idx) -- by default index is the last index if not specified.
 # this methods return the popped value

print(movie)
print(movie.pop())
print(movie)
print(movie.pop(1))
print(movie)
# print(movie.pop)

# -------------** del Operator --------
# print(del movie[0]) # syntax error
del movie[0]
print(movie)

# remove method -- list.remove(item in single quote ) -- remove only if item is present and return none

new_fruits = ["apple" , "banana" , "kiwi" , "pear" , "orange" , "apple" , "banana"]
print(new_fruits)
print(new_fruits.remove('pear'))
print("Pear is removed from the list ",new_fruits)
# new_fruits.remove('Roshan') # item not in list error
new_fruits.remove('apple') # first occurence of apple will be deleted
print("Tried to removed ",new_fruits)

# to add item in list -- append , extend , insert
# to delete data from list -- pop , remove , del

# check item present in list or not

if 'apple' in new_fruits:
    print("apple is present")
else:
    print("Not present")


#--------- some useful methos in list ----
new_list = ['orange' , 'apple' , 'pear' , 'banana' , 'kiwi' , 'apple' , 'banana']
print(new_list.count('apple')) # returns the count of item in list
print("return new sorted list",sorted(new_list))# don't sort the original list but returns a new sorted list
print("original list remianed same ",new_list)
print("list.sort() -> sorts the original list and return none ",new_list.sort()) # sorts the original list
print(new_list)
temp_list = [1,2.9,True,"Roshan" ,["hi",False,None]]
print("Trying to sort hetrgeneous list")
# temp_list.sort() # can't sort this hetregenous list
# print("sorting done ")
print(temp_list)
print("list_name.clear() return ",temp_list.clear())
print(temp_list)
print("list.copy() return the copy of list  " ,  new_list.copy())
new_list_copy = new_list.copy()
print(new_list_copy)



#--------------** List Comparison**----------
# is keyword vs ==
name1 = ["a" ,'b','c','d']







