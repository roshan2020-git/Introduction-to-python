# instance methods
l = [1,2,3]
print(l)
# here we have create an instnace/object named l of list class
# some methods of list class
# pop(defalult index is last index)
l.pop() # last element remove
print(l)
list.pop(l) # is similar to l.pop()
print(l)
l.append('roshan') # append() method add an element in the last of list
print(l)
list.append(l , list(range(1,5)))
print(l)
# Methods are the functions which are defined inside the class
# any class method can only operate on the instance of same class


class Person:
    def __init__(self , first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        return self.age>=18





# creating instance of class Person
p1 = Person("Roshan" , "Gupta" , 22)
print(p1)
print(p1.first_name , p1.last_name , p1.age ) # here we don't need to pass first argument self which is the object itself
# pyhton compiler automatically pass the first argument i.e self which is object itsef bcz before creating any object we use class_name()
# by seeing the class_name compiler knows which kind of obj is going to be created
print(p1.full_name()) # we can alos write Person.full_name(p1)
print(Person.full_name(p1))
print(p1.full_name() is Person.full_name(p1)) # since both will be at different memory location hence False
print(p1.full_name() == Person.full_name(p1)) # both has same value hence True

print(p1.is_adult())
print(Person.is_adult(p1))
# whenever we call any method compiler
# the above call method will execute like : Person.full_name(p1)
# we  don't need to pass first argument otherwise it will gave error



# p2 = Person(Person ,"Rohit" , "Kumar" , 23 ) # TypeError: Person.__init__() takes 4 positional arguments but 5 were given
# print(p2)
# print(p2.first_name,p2.last_name, p2.age)

# exercise 2 :
# In the Laptop class define a method which gives the discount of price of laptop

class Laptop:
    def __init__(self , brand , model , price):
        self.brand_name = brand
        self.price = price
        self. model_name = model

    def apply_discount(self , discount):
        '''
        It return the price after applying the discount 
        :param discount:
        :return:
        '''
        actual_price = 100 - discount
        self.price = (self.price * actual_price)/100
        return self.price



lap1 = Laptop("acer" , "Aspire 7" , 50000)
print(lap1.brand_name , lap1.model_name , lap1.price)
print(f"Price after applying discount of 40% will be :{lap1.apply_discount(40)}")