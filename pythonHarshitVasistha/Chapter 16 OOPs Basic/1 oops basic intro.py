# OOPS stands for Object Oriented Programming
# OOPs is a style/way to write a code
# very helpful to creating real world program

# class , object(instance) , method
# class is a blueprint of an object which has some data member and function/method associated to them


l = [1,2,3,4]
l.append(8)

# python me her chiz ek object hai

# ------ *** Create your first class *** ----------
# INIT method is same as constructor of a class
# constructor is used to initalize the data associated to it

class Person: # in older version of python we use () after class name
    def __init__(self,first_name , last_name , age): # self is same as this keyword and it's a must parameter for init
        # instance variable intialization
        print("__inti__ method i.e constructor is called ")
        self.first_name = first_name # instance variable first_name is intialized with first name
        self.last_name = last_name # instance variable last_name is intialized with last_name
        self.age = age # # instance variable age  is intialized with first age


# here the data members of this class are first_name , last_name , age
# self k saath . me data members ka name likhte hai and = baad hum constructor me passed
# values ko current object  k data members ko value assign kr dete hai jisse hmara
# object intialisez ho jata hai
# now us object par methods laga kr apna task complete kr skte hai

p1 = Person('Roshan' ,"Gupta" , 21)
print(p1) # prints the memory loacation at which p1 object is present
print(p1.first_name , p1.last_name , p1.age)

p2 = Person('Rohan','Singh' , 27)
print(p2)

print(p2.first_name , p2.last_name , p2.age)

# self is same as this keyword
# as this is a pointer to current object self is also a pointer to current object
# it's a convention to used self but we can write anything in place of self

class employee:
    def __init__(employee_instnace , eid , esalary):# instead of self we have named it employee_instnace so this will act as this keyword
        print("constructor or __init__   is invoked ")
        employee_instnace.eid = eid
        employee_instnace.esalary = esalary


mohan = employee(1,10000)
print(mohan.eid , mohan.esalary)
rohan = employee(2,1002828)
print(rohan.eid , rohan.esalary)
shyam = employee(69,1922827)
print(shyam.eid , shyam.esalary)


class Student:
    def __init__(std_inst , roll_no , name , branch): # here instead of self we are using std_inst so wherevere we were using self replace it with std_inst
        # here instead of self std_inst is the pointer to the current object
        print("student constructor is called ")

        '''
        :param roll_no:
        :param name:
        :param branch:
        :return:
        here rool_no , name branch are arguments to constructor which will be assigned to the 
        instance varibale which are std_rool , std_name , std_branch
        '''
        std_inst.std_roll = roll_no # here std_roll is instance variable and value assigned to it is rool_no
        std_inst.std_name = name # here std_name is instance variable and value assigned to it is name
        std_inst.std_branch = branch # here std_branch is instance variable and value assigned to it is branch

        # std_roll ,std_name , std_branch is the instance variable or class variable or object data member
        # so whenver we create an object we will need to use these name using . method to access the value assigned to the object
        # assigned values are roll_no to std_roll data member
        # name to std_name data member
        # branch to std_branch data member



# lets create an object of student class
print()
student1 = Student(2019325 , "Roshan" , "ECE")
print(f"student 1 is at :{student1}")
print(student1.std_roll , student1.std_name,student1.std_branch)

student2 = Student(2019265 , "Hemant" , "ECE")
print(f"student 2 is at :{student2}")
print(student2.std_roll , student2.std_name,student2.std_branch)

student3 = Student(2019317 , "Rahul" , "ME")
print(f"student 3 is at :{student3}")
print(student3.std_roll , student3.std_name,student3.std_branch)

student4 = Student(2019304 , "Pramode" , "ME")
print(f"student 4 is at :{student4}")
print(student4.std_roll , student4.std_name,student4.std_branch)



# it's a good practice to use keyword self and the argument passed to constructor has same name as instance variable or object

# oops exercise 1

# create a laptop class with attributes like brand name , model name , price
# create two objects/instances of your laptop class
class Laptop:
    def __init__(self , brand_name , model_name , price):
        print("Laptop constructor is invoked ")
        self.brand = brand_name
        self.model = model_name
        self.price  = price
        # we can create another instance var  which is combination of two or more instance var which are initialised by constructor
        self.laptop_thing = brand_name+ " " + model_name

# creating instance of Laptop class

lap1 = Laptop("Acer" , "Aspire 7" , 50000)
print("first object lap1 is at :", lap1)
print(lap1.brand , lap1.model , lap1.price , lap1.laptop_thing)

lap2 = Laptop("HP" , "Aspiron 250" , 36000)
print(" second object is at:" , lap2)
print(lap2.model , lap2.brand , lap2.price  , lap2.laptop_thing)

