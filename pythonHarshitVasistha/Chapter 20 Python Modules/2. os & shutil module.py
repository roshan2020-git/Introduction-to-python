import os
import shutil

print(os.getcwd())
print(os.listdir())
os.chdir('movies')
print(os.getcwd())
print(os.listdir())
# print(os.walk('E:\pythonHarshitVasistha')) # <generator object _walk at 0x000001FD4CEDB060>
fileiter = os.walk('E:\pythonHarshitVasistha') # from this os.walk() we can go in depth of file and can check what is present
# fileiter contains the currenr directory name , folder in cur dir , and files in cur dire
for curr_path , folder_names,file_names in fileiter:
    print(f'current path -> {curr_path}')
    print(f'folder names -> {folder_names}')
    print(f'file names  -> {file_names}')
    print('\n \n')

# delete a folder
# rmdir(folder/directory name ) - delets only those folders which are vacant
# os.mkdir('empty')
print(os.getcwd())
print(os.listdir())
# os.rmdir('empty') # moves delete directory in recycle bin
print(os.getcwd())

# folder inside folder
# os.makedirs('new_folder/webseries')
print(os.listdir())

# ------------*** shutil Module ***---------------
# we can delete any folder whether it's empty or not
print(os.getcwd())
# shutil.rmtree('new_folder')
print(os.listdir())
# shutil.copytree() - > copy folder inside other folder
# shutil.copy('file.txt' , 'E:\pythonHarshitVasistha') can copy file in other directory
# shutil.move('file.txt', 'E:\pythonHarshitVasistha/.idea') #we can move file / folder