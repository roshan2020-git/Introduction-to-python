# Multilevel Inheritence
# can we drive more than one class from base class ? " YES"
# MRO - method resolution order
# Method overriding
# isinstnace() , issubclass() -- builtin functions

class Phone: # base class / parent class
    def __init__(self , brand , model_name , price):
        self.brand  = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self , number ):
        return f"calling .. {number}"

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Smartphone(Phone): # drived class / child class
    def __init__(self , brand,model_name , price , ram , internal_memory , camera):
        # Phone.__init__(self , brand, model_name , price)
        super().__init__(brand , model_name , price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = camera
        #method overridng
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} {self.camera}"


class Smartphone2(Phone): # drived class / child class
    def __init__(self , brand,model_name , price , ram , internal_memory , camera):
        # Phone.__init__(self , brand, model_name , price)
        super().__init__(brand , model_name , price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = camera


class Flagship(Smartphone):
    def __init__(self , brand,model_name , price , ram , internal_memory , camera , front_camera , processor):
        super().__init__(brand,model_name , price , ram , internal_memory , camera)
        self.front_camera = front_camera
    # mthod overiding
    def full_name(self):
        return f"{self.brand} {self.model_name} {self.ram} {self.internal_memory}"

    def make_a_call(self , number ):
        return f"calling to {number} from {self.full_name()}"








phone = Phone("Nokia" , "3310" , 1000)
print(phone.full_name())
smartphone = Smartphone("Moto" , "G30" , 17000 , "6Gb" , "64GB" , "20MP")
print(smartphone.full_name())
smartphone2 = Smartphone2("Realme" , "2pro" , 18000 ,"6Gb" , "64GB" , "20MP")
print(smartphone2.full_name())
flagship = Flagship("Realme" , "3pro" , 18000 ,"6Gb" , "64GB" , "20MP" , "80MP" , "snapdragon710")
print(flagship.front_camera)
print(flagship.full_name())

# method resolution order - It shows whenever we call a method then how compiler is going to search for it.
# i.e the order in which the python compiler is going to search
print(help(Phone))
# the above statement will print this
'''
Help on class Phone in module __main__:

class Phone(builtins.object)
 |  Phone(brand, model_name, price)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, brand, model_name, price)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  full_name(self)
 |  
 |  make_a_call(self, number)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
'''
print(help(Smartphone))
'''
Help on class Smartphone in module __main__:

class Smartphone(Phone)
 |  Smartphone(brand, model_name, price, ram, internal_memory, camera)
 |  
 |  Method resolution order:
 |      Smartphone
 |      Phone
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, brand, model_name, price, ram, internal_memory, camera)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Phone:
 |  
 |  full_name(self)
 |  
 |  make_a_call(self, number)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Phone:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
'''

print(help(Flagship))
'''
Help on class Flagship in module __main__:

class Flagship(Smartphone)
 |  Flagship(brand, model_name, price, ram, internal_memory, camera, front_camera, processor)
 |  
 |  Method resolution order:
 |      Flagship
 |      Smartphone
 |      Phone
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, brand, model_name, price, ram, internal_memory, camera, front_camera, processor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Phone:
 |  
 |  full_name(self)
 |  
 |  make_a_call(self, number)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Phone:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None

'''
# method overriding prove
print(phone.full_name())
print(phone.make_a_call(8923817))
print(smartphone.full_name())
print(smartphone.make_a_call(928228))
print(flagship.full_name())
print(flagship.make_a_call(9281830))


# isinstance() is used to check whether the instance belong to a class or not
print(isinstance(phone, Smartphone))
print(isinstance(phone, Phone))
print(isinstance(smartphone , Flagship))
print(isinstance(flagship, Flagship))
print(isinstance(flagship, Smartphone))
print(isinstance(flagship, Smartphone2))
print(isinstance(flagship , Phone)) # retuns true cuz flagship class obj inherited the smarphone class and smartphone class inherites Phone class

'''
Every obj of child is an instance of all of it's parent class

'''
print("issubclass() method")
# issubclass() --- to check whether a class is the child class of parent class or not
print(issubclass(Smartphone,Flagship))
print("checking for Flagship class ")

print(issubclass(Flagship , Smartphone))
print(issubclass(Flagship , Smartphone2))
print(issubclass(Flagship , Phone))
print(f"each class is a subclass of itself: {issubclass(Phone,Phone)} ")
print(issubclass(Phone , Smartphone))
print(issubclass(Phone , Flagship))
print("checking for Smartphone class ")
print(issubclass(Smartphone, Phone))
print(issubclass(Smartphone,Smartphone))
print(issubclass(Smartphone,Smartphone2))
print(issubclass(Smartphone , Flagship))

print("checking for Phone class ")
print(issubclass(Phone, Phone))
print(issubclass(Phone,Smartphone))
print(issubclass(Phone,Smartphone2))
print(issubclass(Phone , Flagship))


