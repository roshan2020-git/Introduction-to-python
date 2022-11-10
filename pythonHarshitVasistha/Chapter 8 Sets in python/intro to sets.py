'''
set is an unordered collection of unique item
in set we CAN NOT store list , tuple , dictionary
'''
set1 = {1,2,3,1,2,3,4,5}
print(f"set is {set1} and length of set is  {len(set1)}")

list1 = [1,2,3,1,2,3,4,5,6,6,7,8,9]
# remove duplicate from list
set2 = set(list1)
print(f"list is: {list1} and set derived from list is {set2}")
list2 = list(set2)
print(f"new unique elements list from set {set2} is {list2}")

#--------** methods of set***--------

# adding element in set
#syntax - set_name.add(object)
set1.add(None)
set1.add(69)
# set1.add([1,2,3])
# set1.add(set([1,2,3]))
# set1.add["string"]
# set1.add((1,2,3))
print(set1)

# remove element from set
# syntax - set_name.remove(key)
removed_item_from_set = set1.remove(2) # removes the key and return None
print(f"removed item is : {removed_item_from_set} and return type of remove method is {type(removed_item_from_set)}")
print(set1)
# set1.remove(82838) # will throw keyError cuz key is not present

# discard method -- delete the key if present in set otherwise don't delete and don't return error and return type is None
discarded_item = set1.discard(1) # Dont throw error if key is not present
print(f" discarded element is : {discarded_item} and return type of discard method is {type(discarded_item)}")
discarded_item1 = set1.discard(928281) # Dont throw error if key is not present

print(f" discarded element is : {discarded_item1} and return type of discard method is {type(discarded_item1)}")

# clear() method
print(f"Before clearing set2 is :{set2}")
print(f"type of clear(_) method is",set2.clear())
print(f"set2 now after clearing is : {set2}")

# copy method

s_copy = set1.copy()
print(f"set1 is : {set1} and copy of set1 is : {s_copy} and both are at different memory location {not (set1 is s_copy)}")
s_copy1 = set1 # this won't make a copy
print(f"Does s_copy1 = set1 points to same obj of same memory location : {s_copy1 is set1}")

for item in set1:
    print(item,end=",")
print()
# set Maths - union -> | and intersection -> &
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1 | s2 # union of two set
print(f"union of set {s1} and {s2} is :{s3}")
s4 = s1 & s2
print(f"Intersection of set {s1} and {s2} is :{s4}")




