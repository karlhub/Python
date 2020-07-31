# Use of Python packages

# Packages installation:
#   1) Install pip from Python url: https://pip.readthedocs.io/en/stable/installing/ storing package in the same directory as rest of Python scripts
#   2) From OS Prompt type: python get-pip.py
#   3) Type pip3 to know the usage of the command pip
#   4) Type pip3 install numpy to install package Numpy (efficent working with Arrays)
#   5) Type pip3 list to know the packages installed so far.
# Info about how packages (or modules) work: https://docs.python.org/3/tutorial/modules.html

# Start using packages - Numpy in this case
import numpy as np # In case we only need to import 1 specific function: "from numpy import array". In this case, there is no need to put the prefix "numpy." when calling the function.
ar=np.array([1,2,3])
print("Type:",type(ar),"Array:",ar)

# Data types in Numpy (https://www.numpy.org/devdocs/user/basics.types.html). NumPy numerical types are instances of dtype (data-type) objects, each having unique characteristics.
x=np.float32(1.0)
print("np.float32(1.0):",x,"Type:",type(x))

y=np.int_([1,2,3])
print("np.int_([1,2,3]):",y,"Type:",type(y))

y1=np.intc([4,5,6])
print("np.intc([4,5,6]):",y1,"Type:",type(y1))

y2=np.double([7,8,9])
print("np.double([7,8,9]):",y2,"Type:",type(y2))

z=np.arange(5,dtype=np.uint8)
print("np.arange(5,dtype=np.uint8)",z,"Type:",type(z))

z1=np.arange(5,dtype=np.double)
print("np.arange(5,dtype=np.double)",z,"Type:",type(z1))

# Using own developed package (module) - Fibinacci
import Programa_18_Python_Module_Fibo as fibo
f=int(input("Number:"))
print(fibo.fib(f))
print(fibo.fib2(f))
print(fibo.__name__)

print ("=> End of program")
