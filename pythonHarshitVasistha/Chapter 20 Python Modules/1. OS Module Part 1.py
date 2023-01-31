import os
print(os.getcwd()) # return current working directory
# os.chdir(r'pathname') # directory changes
# os.mkdir('movies') # make directory
# os.mkdir(r'path\directoryname')
print(os.getcwd())
# os.mkdir('movies') # will give an error file already exist
print(os.path.exists('movie'))
if os.path.exists('movies'):
    print("already exist")
else:
    os.mkdir('movies')

# file creation
open('file.txt' , 'a').close() # only one single file will be created and don't give error on further execution
# os.listdir(path) -> list outs files folder inside the current path directory
print(os.listdir()) # list out files in cwd
# 2 ways we can list the path of file in cwd
# method 1
print(" Printing path of all current files  using method 1 ")
for item in os.listdir():
    cur_path = os.getcwd();
    print(cur_path + '\\' + item)

print(" Printing path of all current files using method 2 ")
# method 2
for item in os.listdir(): # we can also pass the path to get item of that directory
    path = os.path.join(os.getcwd(), item)
    print(path)
