# 3 problems exist in below class
# solving then using getter , setter and decorator


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    def make_a_call(self, phone_number):
        print(f"caliing {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


p1 = Phone('Nokia', '1100', -1000)
print(p1.brand)
print(p1.model_name)
print(p1._price)
p1._price = 1000  # changing the
print(f"updated price is : {p1._price}")

print(p1.complete_specification)

# 3 - problems  in above class
'''
1. _price is taking negative value 
2. if we update the price it's not getting refelected in complete specificaion
3. if we setting negative value to price it's ge
'''


# solving these problems
class New_Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # if price>0:
        #     self._price = price
        # else:
        #     self._price = 0
        self._price = max(price, 0)
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def make_a_call(self, phone_number):
        print(f"caliing {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

# we know while creating the obj the constructor is called hence whatever input is given will be assigned to data member accordingly
# hence in complete_specification which is an instance variable  the data is get assigend
# that's why updation doesn't get reflected in it
# to get rid of this, make a method which prints complete specification
p1 = New_Phone('Realme' , '3 Pro ' , 18000)
print(p1.__dict__)
print(p1.complete_specification())
p1._price = 19000
print(p1.__dict__)
print(p1.complete_specification())



# Property Decorator
'''
@property is already defined decorator in python which converts  any instance method into a property i.e the 
instnace method gets converted into an instance variable 
while calling that method we don't need to put () 
'''


class New_Phone2:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name

        self._price = max(price, 0)
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    # getter and setter
    @property
    def price(self):
        return self._price
    # getter k baad hi setter likhna chhaiye
    @price.setter
    def price(self , new_price):
        self._price = max(new_price , 0)



    def make_a_call(self, phone_number):
        print(f"caliing {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

p1 = New_Phone2("iphone" ,'14 pro max' , 120000)
print(p1.__dict__)
print(p1.complete_specification) # don't need to put () cuz it's no longer a method . it's an instance variable
p1._price = -12000 # we are able to set this negative value to handle this we will use getter and setter
print(p1._price)
p1.price = 200 # now using @property we make a instance variable price which can be used to get and set value of _price
print(p1._price)
print(p1.__dict__)
p1.price = -1010
print(p1._price)
p1._price = -69 # we can still change this price but we have a better method to set and get _price 
print(p1._price)