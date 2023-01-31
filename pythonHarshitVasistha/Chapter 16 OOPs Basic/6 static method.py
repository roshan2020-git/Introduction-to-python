# Static Method
# class method has relation will the class and instnace method has relation with the instance of the class
# Static Method has no relation will the class and the object
# static method has some logical connection with our class i.e why we use it
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
    # class method as a constructor
    @classmethod
    def from_String(cls, string):
        first,last,age = string.split(',')
        Person.count_instance += 1
        return cls(first,last,int(age))

    # Static method
    @staticmethod
    def hello():
        print("Hello ,Static Method is called ")

    # instance methods --> function will perform some action on instance variable of a class
    def get_full_name(self):
        ''' this is an instance method of Person class'''
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        ''' this is an instance method of Person class'''
        return self.age >= 18


p1 = Person("Roshan" , "Gupta" , 21)
p2 = Person("Harshit" , "Vasistha" , 25)

Person.hello()