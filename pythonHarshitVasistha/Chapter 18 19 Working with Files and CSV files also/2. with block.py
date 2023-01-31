# with block is used to read write are do anything with file

with open('file1.txt') as f: # we don't need to close the file default mode is read i.e r mode
    data = f.read()
    print(data)
# file has been already closed we don't need to do f.close()
print(f.closed)
# mode to write in file are w , a , r+ mode
# r+ mode can be used to read and wirte the file
# w mode - used when
with open('file1.txt' , 'w') as f: # if file1.txt doesn't exist then it will create
    f.write("Hello everything has been overwrite ") # overwrite everything and prints
    # data = f.read()
    # print(data)
with open('file1.txt' , 'a') as f: # if file1.txt doesn't exist then it will create
    f.write("\nPsomething is added in it \n ")
    # f.read()

with open('file1.txt' , 'r+') as f: # r+ don't create a file if file is not present already
    f.seek(len(f.read()))
    f.write(" added using r+ mode") # by default it starts overwiritng from the begining
    f.read()


# writing content of file1 in file 2
with open('file1.txt' , 'r') as rf:
    with open('file2.txt' , 'w') as wf:
        wf.write(rf.read())




