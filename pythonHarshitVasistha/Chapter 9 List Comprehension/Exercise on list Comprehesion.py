'''
# Problem 1
'''
# define a fucntion that takes list of strings as argument
# return list containing reverse of each string use List Comprehension

'''


# using normal method
# method 1 - returning new list
def reverse_list(l):
    new_list = []
    for string in l:
        new_list.append(string[::-1])
    return new_list


# changing the original list and then return it
def reverse_list_original(l):
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return l


# using list comprehension

def reverse_using_list_comprehension(ls):
    reverse_ls = [string[::-1] for string in ls]
    return reverse_ls


# one liner code using list comprehesnion
def reverse_using_list_comprehension_short(ls):
    return [string[::-1] for string in ls]


string = ['abc', 'xyz', 'pqr'] 
print(f"original list is : {string}")
print(f"using method 1 returnning new list which is : {reverse_list(string)}")
print(f"original list is not changed  : {string}")
print(f"Now using method 2 to update the original list : {reverse_list_original(string)}")
print(f"original list is now changed to :{string}")
print(f"new list using list comprehesnion func :{reverse_using_list_comprehension(string)}")
print(f"original list is:{string}")
print(f"new list using list comprehesnion func short:{reverse_using_list_comprehension_short(string)}")
print(f"original list is:{string}")

'''
'''
# List Comprehension with if Statement
# syntax - > new_list_name = [appendingValue forLoop if conditon]

numbers = list(range(1,11))
print(numbers)

even_num = []
for i in numbers:
    if not(i & 1):
        even_num.append(i)

print(even_num)
print("using list comprehesnion with if statement")

even_num1 = [i for i in numbers if i%2==0]
even_num2 = [i for i in range(1,11) if not(i%2)]
print(even_num1)
print(even_num2)
odd_nums = [i for i in range(1,11) if i&1]
print(odd_nums)
'''


# problem 2 - given a list(hetreogeneous)
# return a list which has only intgeres typecast to string which are presnt in given list
def num_to_string(ls):
    return [str(i) for i in ls if (type(i)==int or type(i)==float) ]

print(num_to_string([True,False,[1,2,3],1,1,0,3]))


# List comprehesion with if else
# syntax:  [appendExpression if(cond)  else statement  forLoop]
nums = list(range(1,11))
print(nums)
for i in range(len(nums)):
    var = nums[i]
    if var&1:
        nums[i]  = -var
    else:
        nums[i] = var**2
print(nums)

# using list comprehension
new_list = [i*2 if(i%2==0) else -i for i in nums]
print(new_list)

# list comprehension in nested list
example = [[1,2,3] ,[1,2,3],[1,2,3]]
# ApeendingValue = [1,2,3] which can also be generated using list comprehesnion

nested_comp = [[i for i in range(1,4)] for j in range(3)]
nested_comp1 = [[i for i in range(1,4)] for i in range(3)] # same as above .. we can use any varible name i,j,k bacuse it has no relation with i so won't throw error
print(nested_comp)
print(nested_comp1)


# list Comprehension Summary
print("list of natural number upto 10")
print([i for i in range(1,11)])
print([i**2 for i in range(1,11)])
print([i**3 for i in range(1,11)])
print([i for i in range(1,11) if not(i&1)])
# print([i if not(i&1) for i in range(1,11) ]) # else expected error
print([i*2 if not(i&1) else -i for i in range(1,11)])
print([ [i for i in range(1,4)] for j in range(3)])




