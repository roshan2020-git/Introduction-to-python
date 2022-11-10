# problem 1
# def a ducn which take input a list and return a list where first letter is capital of each element
# if we pass another parameter reverse (default = false) then reverse the element and the capitalise the first
def first_capital(ls):
    return [name.capitalize() for name in ls]

print(first_capital(['roshan','ram','rishish','ramezh']))

def first_capital_kwargs(ls ,**kwargs):
    if kwargs.get('reverse_str') == True: # get() method returns True if key is present
        return [name[::-1].title() for name in ls]
    else:
        return [name.title() for name in ls]

print(first_capital_kwargs(['roshan','ram','rishish','ramezh']))
print(first_capital_kwargs(['roshan','ram','rishish','ramezh'] , reverse_str=True))


