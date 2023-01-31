# csv stands for comma separated value

from csv import reader # reading csv file using reader function
with open('temp.csv' , 'r') as f:
    csv_reader = reader(f) # reader return an iterator so csv_reader stores that iterator
    print(csv_reader) # <_csv.reader object at 0x000002DA9364B760>
    print(type(csv_reader) )
    # next(csv_reader) # to go to next row so that heading row don't get printed
    # we can run only one time loop in any iterator
    for row in csv_reader: # or list(csv_reader) to run loop as many times as we want
        print(row)


# read csv file using DictReader function -> ordered dctionary

from csv import  DictReader # DictReader is better than Reader Method
with open('temp.csv' , 'r') as f:
    csv_reader1 = DictReader(f,delimiter = '|') # here we can pass the delimiter
    print(csv_reader1)
    print(type(csv_reader1))
    for row in csv_reader1:
        print(row['name'])
        print(row['email'])


# wite in csv files

from csv import  writer  # writer method
with open('new_csv' , 'w' , newline="") as f:

    csv_writer = writer(f) # return an object which can be used to write in csv file
    print(csv_writer , type(csv_writer))
    '''
    # methods - writerow , writerows
    csv_writer.writerow(['name' , 'countries'])
    csv_writer.writerow(['Roshan' , 'India'])
    csv_writer.writerow(['Biden' , 'USA'])
    csv_writer.writerow(['XingPing' , 'China'])
    '''
    # writerows takes input as list of list
    csv_writer.writerows([['name' , 'countries'],['Roshan' , 'India'],['Biden' , 'USA'],['XingPing' , 'China'],['Modi ji' ,'INDIA']])



# write csv file using DictWriter (better than writer)
from csv import DictWriter
with open('final.csv' , 'w' , newline="") as f:
   csv_writer =  DictWriter(f , fieldnames=['firstname' , 'lastname' , 'age']) # we need to specify header
   csv_writer.writeheader()
   # writerow , writewrows
   csv_writer.writerow({
       'firstname':'Roshan',
       'lastname':'Gupta',
       'age':20
   })
   csv_writer.writerow({
       'firstname':'Roshan',
       'lastname':'Gupta',
       'age':20
   })
   csv_writer.writerow({
       'firstname':'Roshan',
       'lastname':'Gupta',
       'age':20
   })
# writerows-> [ dict , dict , dict] --> dictionaries inside list
   csv_writer.writerows([{'firstname':"Rohan" , 'lastname':'Singhaniye' , 'age':20},
                      {'firstname':"soham" , 'lastname':'Singhaniye' , 'age':20},
                      {'firstname':"Shyam" , 'lastname':'Singhaniye' , 'age':20},
                      {'firstname':"Ronit" , 'lastname':'Singhaniye' , 'age':20}
                      ])

