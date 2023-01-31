# for read -> reader , DictReader
# for write -> writer DictWriter

from csv import DictReader , DictWriter
with open('new_csv' , 'r') as rf:
    with open('new_csv2' , 'w',newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf , fieldnames=['first_name' , 'last_name', 'age'] )
        csv_writer.writeheader()
        for row in csv_reader:
            fname , lname,age = row['name'] , row['countries'] , row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age': age
            })


