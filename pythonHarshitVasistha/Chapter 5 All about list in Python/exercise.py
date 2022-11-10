# 1. return square of element of list
def square_of_list(l):
    for i in range(len(l)):
        l[i] *= l[i]  # changes will occur in the original list
    return l


l1 = list(range(1, 11))
print("Original list", l1)
# print("Reversed list using reverse method it return NONE " , l1.reverse())
# print(l1)
print("Updated list", square_of_list(l1))  # original list will changed


# 2. reverse of list

def reverse_list(l):
    return l[::-1]


def reverse_list2(l):  # return a new list which is reversed wrt original
    reverse = []  #
    for i in range(len(l)):
        idx = len(l) - i - 1
        reverse.append(l[idx])
    return reverse


def reverse_pop_append_method(l):
    rev = []
    while l:
        ele = l.pop()
        rev.append(ele)
    return rev


# list.reverse() -- reversed the original list and return None
print("original list", l1)
print("new reversed list ", reverse_list(l1))
print("original list", l1)
print("reverse list using indexing method ", reverse_list2(l1))
print("original list ", l1)
print("reverse using pop append method is ", reverse_pop_append_method(l1))

# 3 reverse ecah elemnt value of a list
# ['abc' ,'tuv' ,'xyz'] --> ['cba' , 'vut' ,'zyx']

def reverse_each_element(lt): # updation occurs in same list and return the list
    for idx in range(len(lt)):
        lt[idx] = lt[idx][::-1]
    return lt


def reverse_each_element_not_change_original(l):
    new_list=[]
    for i in l:
        new_list.append(i[::-1])
    return new_list

lt = ['abc' ,'tuv' ,'xyz']
print("Original list before reversed " , lt)
print("Updated list after reversal ", reverse_each_element(lt))
print("new list after reversal of original list ele " , reverse_each_element_not_change_original(lt))
print("Original updated list remain the same " , lt)

# 4 filter odd even elem of list

list1 = list(range(1,11))
def filter_odd_even(l):
    filtered_list = [[] ,[]] # [[odd],[even]]
    for _ in l:
        if _ & 1:
            filtered_list[0].append(_)
        else:
            filtered_list[1].append(_)
    return filtered_list


print(filter_odd_even(list1))

# 5. common in two list
# method 1: using two loops


def common_in_list(l1 , l2):
    common_element = []
    for _ in l1:
        for __ in l2:
            if __ == _ :
                common_element.append(__)

    return common_element


# Method2 : using single loop

def common_ele_in_list(l1,l2):
    ans = []
    for i in l1:
        if i in l2:
            ans.append(i)
    return ans


l1 = [1,2,3,4,5]
l2 = [2,3,4,7,9]
print(common_in_list(l1 ,l2))
print(common_ele_in_list(l1,l2))

# ----------** min max function in python
num = [1,2,828]
print(min(num))
print(max(num))


def max_diff(l):
    return max(l) - min(l)


print(max_diff(num))


def count_no_of_list_inside_list(l):
    ct=0
    for _ in l:
        if type(_) == list : # type(_) == type(l)
            ct+=1
    return ct


print(count_no_of_list_inside_list([[] , 1,2,3,[[]],[]]))