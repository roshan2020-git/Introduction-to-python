# reading in parse

with open('lorem2000.txt' ,'r' ,encoding= 'utf-8') as f:
    data = f.read(100) # reads only 100 char at a time
    while(len(data)>0):
        print(data)
        data = f.read(100)

