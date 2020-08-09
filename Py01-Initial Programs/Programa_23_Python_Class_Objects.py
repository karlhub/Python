# A simple class example
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        self.data = []

# Class instantiation uses function notation.
# Just pretend that the class object is a parameterless function that returns a new instance of the class.
x = MyClass() # creates a new and initialized instance of the class and assigns this object to the local variable x.

print ("Type x: ",type(x))
print (x.i)
print (x.f())
print (x.__doc__)

# x.f is a method object, and can be stored away and called at a later time.
xf = x.f
print (xf())

# The special thing about methods of classes is that the instance object is passed as the first argument of the function.
# In our example, the call x.f() is exactly equivalent to MyClass.f(x).

# Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.
# For example, the following piece of code will print the value 16, without leaving a trace:
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# A more complex class example with initialization parameters
class Complex:
    """A more complex class"""
    def __init__(self,realpart=3.0,imagpart=-4.5):
        self.r = realpart
        self.i = imagpart

y = Complex()
print (y.r,y.i)
y = Complex(77,12)
print (y.r,y.i)
