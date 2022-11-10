# Problem 1
'''
define a func which take input as a number or list of number which are orderaly stored i.e tuple or list
beacuse in args we can pass only those arguments which are ordered and hashbale and can be iterable
input [1,2,3]
output = [1,8,27]
 if user didn't pass any args print you didn't pass any argument
 else return output list

 # NOTE: use list comprehension
'''

# short cut to check any data sturucture is empty or not
# if data_stru ---> this staemente is true when data_struc is not empty and false when data structure is empty
def check_empty(any_data_structure):
    if any_data_structure:
        print(f"{type(any_data_structure) } is not empty")
    else:
        print(f"{type(any_data_structure) } is  empty")



def problem1(*args):
    output = []
    if args == ():
        return "Hey you didn't pass any args"
    else:
        for i in args:
            output.append(i**3)
    return output


def problem1_short(*args):
    # output = []
    if not args:
        return "Hey you didn't pass any args"
    else:
        return [i**3 for i in args]
    #     for i in args:
    #         output.append(i**3)
    # return output

print(problem1(2,3,4,))
print(problem1())
print(problem1(*[1,2,3]))
print(problem1(*(1,2,3)))
print("printing ans using list comprehension ")
print(problem1_short(2,3,4,))
print(problem1_short())
print(problem1_short(*[1,2,3]))
print(problem1_short(*(1,2,3)))

def to_power(num , *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args "



print("printing ans using list comprehension: again ")
print(to_power(2,2,3,4,))
print(to_power(2))
print(to_power(2,*[1,2,3]))
print(to_power(2,*(1,2,3)))



# Problem 2