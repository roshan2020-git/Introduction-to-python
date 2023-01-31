# Class Variable is variable related to class which has constant or same value for each object of the class
# Let's define a circle class
class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def circurmference(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * (self.radius ** 2)


c1 = Circle(4, 3.14)
print(c1.radius, c1.pi, c1.area(), c1.circurmference())
c2 = Circle(5, 3.14)
print(c2.radius, c2.pi, c2.area(), c2.circurmference())


# for every object Pi value is going to be remained same
# so every object is going to have memory to store data of pi
# for better memory management we define a class varible which belong to class and each object is going to have same value
# so we don't need to have extra memory to stroe that value
# it is a better memory management


class Circle2:
    pi = 22 / 7  # class variable
    # this class varible can be accesed by ClassName.ClassVariableName i.e Circle.pi which has value 22/7
    '''
    Class Variable is variable related to class which has constant or same value for each object of the class
    '''

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * self.radius * Circle2.pi

    def area(self):
        return Circle2.pi * (self.radius ** 2)


# print(Circle2.__doc__)
# print(help(Circle2))
new_c1 = Circle2(4)
new_c2 = Circle2(5)
print(new_c1.radius, new_c1.area(), new_c1.circumference())
print(new_c2.radius, new_c2.area(), new_c2.circumference())


# suppose we have apply discount on every laptop
class Laptop:
    discount = 10
    def __init__(self , brand , model , price):
        self.brand_name = brand
        self.price = price
        self. model_name = model

    def apply_discount(self):
        '''
        It return the price after applying the discount
        :param discount:
        :return:
        '''
        actual_price = 100 - Laptop.discount
        self.price = (self.price * actual_price)/100 # updating the price of Laptop
        return self.price # returning the updated value of laptop


lap1 = Laptop("ACER" , "ACEPIRE" , 50000)
lap2 = Laptop("HP" , "Aspiron" , 60000)
print("lap1 price before discount" , lap1.price)
lap1.apply_discount()
print(f"lap1 price after applying 10% discount is : {lap1.price}")


# what if we need to change the value of Class variable
# suppose for HP laptop we have to give discount of 20% then what to do?

Laptop.discount = 20 # this statement will change the value of discount from 10 to 20 for every object created after this
print("Before discount laptop 2 has price :",lap2.price)
lap2.apply_discount()
print(f" lap2 price after 20% discount is :{lap2.price}")
Laptop.discount = 10 # let's change it back to 10

# printing all data member and their value of an object/instance
print("Printing all data member ana their value of current created objects ")
print(c1.__dict__)
print(c2.__dict__)
print(new_c1.__dict__)
print(new_c2.__dict__)
print(lap1.__dict__)
print(lap2.__dict__)

# Now if we wan't to change the discount for particular laptop
# let's see how can we do it
lap3 = Laptop("Asus" , "vivo v14" , 80000)
print(lap3.__dict__)
lap3.discount = 30 # a new data member will be added maned discount which has value 30 but the Class variable discount will
# remianed same
print(lap3.__dict__)
print(f" price of laptop 3 after applying discount :{lap3.price}")
lap3.apply_discount() # discount of 10% will be applied not 30%
print(f" price of lap3 after 10% discount is : {lap3.price}")
'''
during defining class we have used Laptop.discount to claculate the discount 
if we use self.discount instead of Laptop.discount then the discount data member of that object will be 
applied to it not the class variable 
'''
# To apply discount on particular intance first add a data member to it using , operator
# while defining apply_discount() method use self instead of class variable so that the discount which is associated to that
# object will be applied ot it not the class variable discount
# if any object don't have discount data member in that case the the default class varibale discount will take place in that object

class Laptop2:
    discount = 10
    def __init__(self , brand , model , price):
        self.brand_name = brand
        self.price = price
        self. model_name = model

    def apply_discount(self):
        '''
        It return the price after applying the discount
        :param discount:
        :return:
        '''
        actual_price = 100 - self.discount # instead of Class varible discount we have used the object varible or data member discount
        # if object has discount data member then it will apply that discount otherwise it will apply the default discount which is class variable value of 10
        self.price = (self.price * actual_price)/100 # updating the price of Laptop
        return self.price # returning the updated value of laptop

lap4 = Laptop2("Mi" ,"Notepad" , 40000)
print(lap4.__dict__)
print(f" price of lap2 before discount {lap4.price}")
lap4.apply_discount()
print(f"Default 10% discount is applied then reduced price is:{lap4.price}")
lap4.discount = 20
print(lap4.__dict__)
lap4.apply_discount()
print(f" Extra 20 discount is applied then reduced price is :{lap4.price}")

# ---------***** EXERCISE-3 **** -------------
# create any class and count the no of instnaces of class has been created

class Person:
    count_instance = 0
    def __init__(self,first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_instance+=1


p1 = Person("Roshan" , "Gupta" , 21)
print(Person.count_instance)
p2 = Person("Naresh" , "Singh" , 22)
print(Person.count_instance)


