language = "Python"
'''
1. from left to right indexing start from  0 to size -1
2. from right to left indexing start from -1 , -2 , -3 .... -size
'''
print(language[0])
print(language[-1])
print(language[-6])

#slicing in string or slecting sub sequences

#syntax - stringName[startindex:endIndex:steps] --> sliced the string from start to end-1
# positive value of step is for forward steps and negative is for backward steps


name = "Roshan Kumar Gupta"

print(len(name))
print(name[0:5])#subsequence from 0 to 4 will be printed
print(name[-18:-13])
print(name[0:])
print(name[-18:])
print(name[:18])
print(name[:-1])
print(name[:])
print(name[0:18:1])
print("same as" , name[-18:-1:1])
print(name[0:18:2])
print(name[-1::-1])
print(name[::-1]) # return the reverse the string(doesn't alter the original string)
print(name)
print("Hare Krishna"[:])
print("Hey Brother"[0:5])
print("Hello ji"[::1])
print("Hello ji"[::2])
print("Love you Alot"[::3])
print("Roshan"[3::-1])

username = input("Enter your name ")
print(f"your name in reverse order is {username[-1::-1]}")
print(username)