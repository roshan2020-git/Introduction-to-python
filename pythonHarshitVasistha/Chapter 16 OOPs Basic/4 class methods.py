# class methods Vs instance methods

class Person:
    count_instance = 0  # class variable / Class attribute
    # to access class variable syntax is : class_name.class_var_name for eg: Person.count_instance
    # class method -
    @classmethod  # already defined decorator for creating class method
    def count_instances(cls): # cls is a pointer to current class
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name  # self is a pointer to current object and first_name is instance variable
        self.last_name = last_name
        self.age = age
        Person.count_instance += 1

    # instance methods --> function will perform some action on instance variable of a class
    def get_full_name(self):
        ''' this is an instance method of Person class'''
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        ''' this is an instance method of Person class'''
        return self.age >= 18

p1 = Person("Roshan" , "Gupta" , 22)
p2 = Person("Rohan" , "Agarawal" , 25)
print(Person.count_instances()) # this is good to write . from this it is clear that it is class method

print(p1.count_instances()) # we can also access this class method using obj of that class cuz
# compiler first check for if this is a instance method or not then it will check for class method
# anyone of this found true then it will execute that method
print(Person.__name__)
print(p1.__dict__)
print(p2.__dict__)

