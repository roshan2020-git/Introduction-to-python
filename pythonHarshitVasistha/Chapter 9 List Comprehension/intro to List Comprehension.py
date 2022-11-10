'''
List comprehesion is a shortcut method to create list
'''
# create a list of square of 1 to 10
# Basic Method
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# List comprehension method
# list_name = [ apeendValue  forloop]
squares2 = [i**2 for i in range(1,11)]
print(squares2)

# list of neagtive natural number
# Basic method
neg_nat = []
for i in range(1,11):
    neg_nat.append(-i)
print(neg_nat)
# list comprehension method
negative_natural = [-i for i in range(1,11)]
print(negative_natural)
# create list of first char of already existing list
# Basic Method
names = ['Roshan','kumar','Gupta']
char = []
for name in names:
    char.append(name[0])
print(char)

# List comprehesntion method
new_char = [name[0] for name in names]
print(new_char)