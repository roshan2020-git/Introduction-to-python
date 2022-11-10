# Dictionary comprehension is same as list comprehension
# we can create dictionary in one line

# square = {1:1,2:4,3:9 ......}

# syntax:     { key:valueExpression forloop]
square = {num:num**2 for num in range(1,11)}
square1 = {f" square of {num} is :{num**2}" for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f" square of {k} is {v}")
print(square1)

# count character

string = "aababduuerrkssk"
cc_count = {char: string.count(char) for char in string}
print(cc_count)


# dictionary comprehesion with if else
# syntax: {key:(Appendvalue if cond else appendvalue) for loop}
odd_even = {i:('odd' if (i&1) else 'odd' ) for i in range(1,11)}
print(odd_even)

# set comprehesnion is almost same as dict comprehehsnsion only keys are in set

s= {k for k in range(1,11)}
print(s)

names = ['aba','cde']
s = {char[0] for char in names}
print(s)

