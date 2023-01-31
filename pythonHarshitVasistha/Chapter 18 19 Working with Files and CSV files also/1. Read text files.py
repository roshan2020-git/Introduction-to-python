'''
readfile
open function - curr_file = open(filePath , mode(r,w,) -> returns an object

read method -  curr_file.read() -> return whatever is in curr_file in string format
seek method - curr_file.seek(new_cursor_pos) -> changes the cursor position from cur_pos to new_cursor_pos
tell method - curr_file.tell() -> returns the current position of cursor in file
readline method - curr_file.readline() - reads only one line at a time
readlines method - curr_file.readlines(noOfLines) - lists all the lines in a list , returns a list of all the lines inside the curr_file
# by default it takes all lines but we can explicitly mention no of lines
close method -
'''


f = open('file1.txt' , 'r') # open function takes path of the file as input default mode is read
# f.open(r"filePath" , mode) # use raw string otherwise compiler will treat \n , \t .. as escape sequence characters
# print(f) # return an objec
# data descriptor -
# 1. name -> curr_file.name -> return name of current file which is examined
#2. close  -> curr_file.close -> return true if file is close or false if not closed

print(f.name)
print(f.closed)
print(f'cursor pos is {f.tell()}')

print(f.readline())
print(f.readline())
print(f'cursor pos is {f.tell()}')
f.seek(0)
print(f'cursor pos after applying f.seek(0) is {f.tell()}')
lines = f.readlines(2)
print(lines , len(lines))
for line in lines:
    print(line , end="")
f.seek(0)
print(f'cursor pos after applying f.seek(0) is {f.tell()}')

print(f.read)
print(f'cursor pos is {f.tell()}')
print(f.read() , type(f.read())) # reads the file and return the op in form of string

print(f'cursor pos is {f.tell()}')

print(f.read()) # only one time will be printed
print(f'cursor pos is {f.tell()}')
f.seek(0)
print(f"new cursor pos is after applying seek method {f.tell()} ")
print("Now if we use read method it will print the whole data inside txt file")
print(f.read())
# reading will be done according to the last position of cursor . At first iteration  the cursor is at last positon.
# after that nothing is there hence nothing will be printed
f.close()
print(f.closed)