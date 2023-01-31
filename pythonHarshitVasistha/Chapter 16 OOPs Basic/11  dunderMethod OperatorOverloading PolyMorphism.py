# special magic/dunder method
# operator overloading
# polymorphism - method/function overriding (achieved by inheritance)
# operator and function overloading comes under compile time polymorphism 
class Phone:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_spec(self):
        return f"{self.brand} {self.model}"

    # str , repr dunder method are used to print whatever written inside this  when we pass the obj in print() str is prior if both are writtend
    # in str dunder we wrote nicely formatted string

    def __repr__(self): # repr stands for representation and used by developers to understand about the object
        # return f"{self.brand} {self.price} {self.model}"
        return f"Phone(\'{self.brand}\' ,\'{self.model}\' , \'{self.price}\')" # printing the way we were creating the object

    def __str__(self):
        return  f"{self.brand} {self.model} and price is {self.price}"

    # len dunder to print anything we want
    def __len__(self):
        return len(self.phone_spec())

    # Operator Overloading ( + operator overlaoding)
    def __add__(self, other): # self points to current obj and other points to other obj which is to added to self obj
        return self.price + other.price
    def __sub__(self, other): # self points to current obj and other points to other obj which is to added to self obj
        return self.price - other.price
    def __mul__(self, other): # self points to current obj and other points to other obj which is to added to self obj
        return self.price * other.price

    # we can use __sub__ , __mul__ , __divmod__ , __mod__  etc to overload other operators



class Smartphone(Phone):
    def __init__(self , brand , model , price , ram , preocessor):
        super().__init__(brand , model , price)
        self.ram = ram
        self.processor = preocessor

    # method overiding
    def phone_spec(self):
        return f"{self.model} {self.brand} {self.price} {self.ram} {self.processor}"
    def __len__(self):
        return self.price




l = [1,2,3,4] # here l is an object of list class

print(l) # prints the whole list
p1 = Phone("Nokia" , "3310" , 1000)
p2 = Phone("Realme" , "3310" , 10000)
print(p1) # print address of memorty location wheere p1 is stored(if repr ar str is not defined otherwise str dunder will
# we can use 2 dunder method to print
print(str(p1))
print(repr(p1))

print(p1.__repr__())
print("Printing len of phone spec using dunder method and len function , both will gave same op")
print(len(p1))
print(p1.__len__())

print(p1 + p2)

# method overiding
p_smart = Smartphone("OnePlus" ,"Nord2" , 35000 , "8GB" , "Snapdragon 830")
print(p1.phone_spec())
print(p1.__len__())
print(len(p1))
print(p_smart.phone_spec())
print(len(p_smart))
print(p_smart.__len__())
