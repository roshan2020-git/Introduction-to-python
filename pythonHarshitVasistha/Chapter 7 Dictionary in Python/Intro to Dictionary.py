'''
List is not sufficient to represent real life data that is why we need other data structure
Dictionary  is used to store data in key value pair
Dictionary is unordered collection of data in key value pair
There is no Indexing in dictionary
accessing data can be done using keys
'''

# create dictiobary in python
user = {'name': "Roshan", 'age': 24}
print(user)
print(type(user))

# create dictionary using dict keyword
user1 = dict(name="Roshan Gupta", age=24)
print(type(user1), user1)

# access data from dictionary

print(user['name'])
print(user.keys())  # return <class 'dict_keys'> all keys of dictionary
print(user.values())  # returns <class 'dict_values'> of all values of dictionary

# any type of data can be stored inside the dictionary
# example - int , float , string , list , tuple , dictionary etc etc all data structures

user_info = {
    'name': ' Roshan',
    'age': 24,
    'fav_movie': ["Thor Ragnarok", "Avenger infinity war"],
    'fav_songs': ['Ram siya Ram', 'Parvati boli Shankar se']
}
print(user_info)
print(user_info.keys())
print(user_info.values())
print(user_info['fav_movie'])
print(user_info['fav_songs'])

# dictionary inside dictionary
users = {
    'user1': {
        'name': ' Roshan',
        'age': 24,
        'fav_movie': ["Thor Ragnarok", "Avenger infinity war"],
        'fav_songs': ['Ram siya Ram', 'Parvati boli Shankar se']
    },
    'user2': {
        'name': 'Ramesh',
        'age': 24,
        'fav_movie': ["Thor Ragnarok", "Avenger infinity war"],
        'fav_songs': ['Ram siya Ram', 'Parvati boli Shankar se']
    },
    'user3': {
        'name': 'Roshan',
        'age': 24,
        'fav_movie': ["Thor Ragnarok", "Avenger infinity war"],
        'fav_songs': ['Ram siya Ram', 'Parvati boli Shankar se']
    }
}

print(users)
print(type(users.keys()), users.keys())  # <class 'dict_keys'>
print(type(users.values()), users.values())  # <class 'dict_values'>
print(users['user1'])
print(users['user2'].keys())
print(users['user2'].values())

# dictionary can be used to store and represent complex data

# how to add data inside empty dictionary

empty_dictionary = {}
empty_dictionary['name'] = "myself"
empty_dictionary['age'] = 19
empty_dictionary['movies'] = ["DDLJ", "The Hindu", "The Legend Of Prince Rama"]
print(empty_dictionary)

# in keyword and iteration in dictionary

# in keyword -- used to check whether a key is present in the dictionary or not
if 'name' in empty_dictionary:
    print(f"key name is present")
else:
    print("Not Present ")

if 'movie' in empty_dictionary.keys():
    print(f"key name is present")
else:
    print("Not Present ")

# check if value is present or not
if 'any_value' in empty_dictionary.values():
    print(f"'any_value' is present")
else:
    print("Not present in dictionary values ")

if 19 in empty_dictionary.values():
    print(f"'any_value' is present")
else:
    print("Not present in dictionary values ")

# keys can be anything in dict but mostly the key is intger or string data type

# loops in dictionary
print("keys in the dictonary are")
for keys in empty_dictionary:
    print(keys, end=',')
print()
print("Now printing values inside dictionary")
for values in empty_dictionary.values():
    print(values, end=',')
print()
# <class 'dict_values'>, <class 'dict_keys'> we can't add or delete date from these but can iterate through elements of this data sturctue
# print dict value using key and for loop
print("Printing value of dict using for loop and keys of dict")
for key in empty_dictionary:
    print(empty_dictionary[key], end=",")
print()
# item() method of dictionary returns <class 'dict_items'> [(key,value),(key,value)]
print(type(empty_dictionary.items()), empty_dictionary.items())
print()
print("printing key value using dict.items() method :")
for key, value in empty_dictionary.items():
    print(f"key is {key} and value is {value}")
print()
print("Each element in dict.items() is tuple")

for Tuple in empty_dictionary.items():
    print(Tuple, end=",")
print()

print("Tuple Unpacking :")

for i, j in empty_dictionary.items():
    print(f"key is {i} and value is {j}")

# add data in dictionary
# traditional method
empty_dictionary['fav_song'] = ["Abbc", "ajhdu"]
print(empty_dictionary)

# DELETE data from dic
# syntax - dict_name.pop('key') -- return the key value pair
popped_item = empty_dictionary.pop('fav_song')
print("first popped item :", popped_item, type(popped_item))
print(empty_dictionary)
second_popped_item = empty_dictionary.pop('name')
print("Second popped item :", second_popped_item, type(second_popped_item))
print(empty_dictionary)

# popitem() method in dict_name.popitem() -- randomly delete any key value pair from dictionary and returns it

popped_item_new = empty_dictionary.popitem()
print(f"randomly deleted item from dictionary is {popped_item_new} and type is {type(popped_item_new)}")

# update method in dictionary
# syntax - dict1.update(dict2) -- return None but add element of dict2 in dict1 at the end
dict1 = {
    'name': "Raju",
    'age': 22,
    'fav_movie': ["ABC", "XYZ", None, 202, 2.292],
    'fav_song': ["I'm faded", "Fairy Tale"]
}

dict2 = {
    'name': "Roshan",
    'state': "Uttar Pradesh",
    'hobbies': ['Cricket', 'Reading', 'coading', 'guitar']
}

print(type(
    dict1.update(dict2)))  # if some keys of dict2 are same with dict1 then the previous key value pair gets updated
print(dict1)
print(dict1.update({}))  # dict1 remains same as it is
print(dict1)

# ------** Other methods of dictionary **--------------


# fromkeys() -- used to create dictionary
# syntax - dict.fromkeys(iterable data structure i.e key , default value of each item of iterable data structure i,e value)
# suppose we have to make a dictionary where every key has a default value
# d = {"name": "unknown" , "age": "unknown"}
# fromkeys() method input parameter is list which is an iterable item
d_list = dict.fromkeys(['name', 'age'], 'unknown')
print(d_list)
# fromkeys() method input parameter is tuple which is an iterable item
d_tuple = dict.fromkeys(('name', 'age'), 'unknown')
print(d_tuple)
# fromkeys() method input parameter is string which is an iterable item
d_string = dict.fromkeys("abc", [1, 2, 3])  #
print(d_string)
d_any_type = dict.fromkeys(['name', 'age', 'state'], [None, None])
print(d_any_type)
d_range = dict.fromkeys(range(1, 10), (None, None))
print(d_range)

# get() method --
# generally we access value of dict as dict_name[key] what if key is not Present. then that time we will get key not present error
# to hadle KeyError we use get method
# syntax - dict_name.get(key)
# print(d_range[10]) # KeyError: 10
print(d_range.get(10))  # key 10 is not present but won;t through error instead of this it will throw None

if 10 in d_range:
    print("present")
else:
    print("Not present")

if d_range.get(9):  # if None ---> means the condion is false hence else block will be executed
    print("present")
else:
    print("Not Present")

# clear() method -- used to clear the dict
# print("dict_name.clear() return : ",d_range.clear())
print(d_range)

# copy() method - returns a copy of the dictionary
# d1 is d2 will check if d1 n d2 both points to same dict or not (is checks for memory address)
# d1 == d2 will check if d1 and d2 have same key value pair or not (== checks for values)
d_range_copy = d_range.copy()
d_range_copy1 = d_range  # this won't make a copy , instead of this they will point to same dict
print(f"proof of d_range_copy1 is same as d_range : {d_range_copy1 is d_range}")
d_range_copy1.pop(1)  # popped key from original dict
print(f"printing d_range dict{d_range}")
d_range_copy.pop(2)
print(f"printing d_range dict after deleting key 2 from d_range_copy {d_range}")
print(f"printing d_range_copy dict after deleting key 2 from it{d_range_copy}")

# -----------** More About get() method **-------------


info = {'name': 'Roshan', 'age': 24, 'name': 'Gupta'}  # keys are unigue
print(info)  # name will be overwritten with the value Gupta(which is the last value assigned to key 'name')
print(info.get('name'))  # if key is found return its value
print(info.get('names'))  # key is not found return None (default parametre if key is not found)
print(info.get('names', 'Not Found'))  # returns Not found if key is not present
