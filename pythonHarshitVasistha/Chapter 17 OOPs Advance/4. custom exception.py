'''
python custom exceptions  are used to increase the readability of code
'''
'''
def validate(name):
    if len(name)<8:
        raise ValueError('name is too short')


user1 = input("Enter your name ")
validate(user1)
print(f"Hello {user1}")
'''
# suppose we want to print NameTooShort -> custom error Error insted of ValueError -> inbuilt error

class NameTooShortError(ValueError):
    pass

def validate2(name):
    if len(name)<8:
        raise  NameTooShortError('name is too short')

user2 = input("Enter your name ")
validate2(user2)
print(f"Hello {user2}")