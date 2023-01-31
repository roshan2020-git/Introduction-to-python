class Phone:  # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, phone_number):
        return f" calling.... {phone_number}....."


class Smartphone:

    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, phone_number):
        return f" calling.... {phone_number}....."


phone = Phone("Nokia", "1100", 1000)
smartphone = Smartphone("Realme", "3pro", 166000, '6GB', '128GB', '60MP')
print(phone.full_name())
print(smartphone.full_name())


# here we are not using DRY(Don't repeate yourself) principle

# inheritence
class New_Smartphone(
    Phone):  # Derived / child class , in bracker we pass the parent class which is going to be inherited
    def __init__(self, brand, model_name, price, ram, internal_memoory, rear_camera):
        # two way to inherit base class
        # 1st way
        # Phone.__init__(self,brand,model_name,price) # uncommon way to inherit , in bracket we pass those argu which we want to inherit from base class
        # 2nd way using super()
        super().__init__(brand, model_name,
                         price)  # don't need to pass self only those attributes name (not instnace data member name ) which are to be inherited
        # for eg we have used the attribute name price not instance variable name _price
        self.ram = ram
        self.internal_memory = internal_memoory
        self.rear_camera = rear_camera


phone = Smartphone("Nokia", "1100", 1000, '6GB', '128GB', '60MP')
new_smartphone = New_Smartphone("Realme", "3pro", 166000, '6GB', '128GB', '60MP')
print(phone.full_name())
print(f"{new_smartphone.full_name()} and price is {new_smartphone._price} and ram is {new_smartphone.ram}")
print(f"{new_smartphone.make_a_call(9118612121)}") # new_smartphone inherited the base class properties
print(f"{new_smartphone.rear_camera}")