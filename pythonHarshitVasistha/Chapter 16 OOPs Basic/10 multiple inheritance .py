# multiple inheritance
class A:
    def class_a_method(self):
        return 'I\'m just a class A method '

    def hello(self):
        return 'Hello from Class A'


instance_A = A()
print(instance_A.class_a_method())
print(instance_A.hello())

class B:
    def class_b_method(self):
        return "I\'m just class B method "
    def hello(self):
        return "Hello from class B"

class C(A,B): # inheritance order matters A,B
    pass

instance_c = C()
print("Printting class C which inherites class A and B methods")
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello()) # class method hello method will be run not class B
print(help(C)) # method resolution order
'''
Help on class C in module __main__:

class C(A, B)
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object
 |  
 |  Methods inherited from A:
 |  
 |  class_a_method(self)
 |  
 |  hello(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from B:
 |  
 |  class_b_method(self)

None

'''

class D(B,A): # inheritance order is B , A
    def class_d_method(self):
        return "HEllo from class D"


instance_d = D()
print(help(D))
print(instance_d.hello()) # class B hello method will be called

# we can also use mro() method to check method resolution order of any class
print("priniting using mro() method which prints method resolution order in list")
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print("Printing using __mro__ dunder which prints list of method resolution order")
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
