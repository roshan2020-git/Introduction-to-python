'''
4 pillars of oops are
Encapsulation , Absatraction , inheritence , polymorphism
'''
'''
Topics to be covered -
Encapsulation , Abstarction , some special naming convention , Name Mangling(Not a convention ) 
'''


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    # instance method

    def make_a_call(self, Mob_No):
        print(f"calling {Mob_No}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_msg(self):
        pass # twillio


# Encapsulation - Data binding
# Abstraction - Hiding the complexicity from the user
'''
l = [3,5,71,1]
l.sort() # tim sort algo is used 
print(l) 
# Here we don't know what is written inside the sort method but we are using this method
# this is Abstraction 
'''
# ----------*** some special naming convention ***----------
# everything in python is by default public i.e data member and function of class is accessible everywhere
'''
1. '_name': convention of private name i.e  to show other that this  data member  to be treated as private , start the variable name with underscore
eg: _price , it will be treated a pvt data member 
2. '__name__'  , it is dunder /magic method 

'''
phone1 = Phone('Nokia' ,'1100' , 1000 )
print(phone1._price)
phone1._price = 89 # we can update the _price cuz it's a public data member but to show others that treat this public data member
# as pvt data member we use _ at the starting of variable name but actually everything is public
print(phone1._price)

# name mangling : this is not a convention
class New_Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price # here we are declaring a data member double undescore price i.e __price

    # instance method

    def make_a_call(self, Mob_No):
        print(f"calling {Mob_No}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_msg(self):
        pass # twillio


p1 = New_Phone('Realme' , '3pro' , 17000)
# print(p1.__price) #AttributeError: 'New_Phone' object has no attribute '__price'
# although during decalring the class we have an instance variable name __price
# but while accessing we are getting an error
print("let's print the data members of a instance :")
print(p1.__dict__) # '_New_Phone__price'
# we can see that __price is changed to _New_Phone__price
print(p1._New_Phone__price)
p1._New_Phone__price = 15000 # updating the value
print(p1._New_Phone__price) # it's proven it's a public data member
# python compliler has just changed this data member name to avoid the confusion
# this is called Name Mangling
