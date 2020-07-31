# Use of Python package: Numpy - Numeric Python

# Main functionalities:
#   1) Mathematical operations between lists
#   2) Calculations over entire arrays
#   3) Fast execution
#   4) Easy coding

# Updated reference guide for Numpy arrays: https://www.numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray

# Alternative to Python List: Numpy Array.
import numpy as np

height=[1.73,1.68,1.71,1.89,1.79]
print("Height:",type(height),height)
weight=[65.4,59.2,63.6,88.4,68.7]
print("Weight:",type(weight),weight)

try:
    bmi=weight/height**2
except:
    np_height=np.array(height)
    print("np_height:",type(np_height),np_height)
    np_weight=np.array(weight)
    print("np_weight:",type(np_weight),np_weight)
    np_bmi=np_weight/np_height**2
    print("np_bmi:",type(np_bmi),np_bmi)

# A Numpy array containing different types is converted into an array of strings.
np_mixed=np.array([1.0,"is",True])
print("np_mixed:",type(np_mixed),np_mixed)

# Numpy subsetting
print("np_bmi[1]:",np_bmi[1],type(np_bmi[1]))
print("bmi>23:",np_bmi>23)
print("bmi[bmi>23]",np_bmi[np_bmi>23])

# ndarray stands for n-dimensional array.
print("\n","Creation of 2D array:","\n")
np_2d=np.array([height,weight])
print(np_2d)
print("Dimension (rows*columns):",np_2d.shape) # Shape is an attribute of np_2d

np_2d_mixed=np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,"68.7"]])
print("\n np_2d_mixed:",type(np_2d_mixed),np_2d_mixed)

print("np_2d[0]:",np_2d[0])
print("np_2d[0][2]:",np_2d[0][2])
print("np_2d[0,2]:",np_2d[0,2])
print("np_2d[:,1:3]:",np_2d[:,1:3])
print("np_2d[1,:]:",np_2d[1,:])

print("np_2d*2:",np_2d*2)
print(np_2d*2)

# Basic Statistics and "ndarray" constructor (https://www.numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray)
print("\nBasic Statistics\n")
np_2d=np.ndarray([3,6],dtype=int,order="F")
i=0
while i<3:
    j=0
    while j<6:
        np_2d[i,j]=i+100*j
        j=j+1
    i=i+1
print(np_2d)
print("Average 1st column: np.mean(np_2d[:,0])",np.mean(np_2d[:,0]))
print("Median 1st column: np.median(np_2d[:,0])",np.median(np_2d[:,0]))
print("Average 1st row: np.mean(np_2d[0,:])",np.mean(np_2d[0,:]))
print("Median 1st row: np.median(np_2d[0,:])",np.median(np_2d[0,:]))
print("Correlation of columns 0 and 2: np.corrcoef(np_2d[:,0],np_2d[:,2])",np.corrcoef(np_2d[:,0],np_2d[:,2]))
print("Standard Deviation 1st column: np.std(np_2d[:,0])",np.std(np_2d[:,0]))
print("Sum all data of each column: sum(np_2d[:,:])",sum(np_2d[:,:]))
print("Sum all data: np.sum(np_2d[:,:])",np.sum(np_2d[:,:]))
print("Sort all data of each column: np.sort(np_2d[:,:])",np.sort(np_2d[:,:]))

# ndarray constructor mode 1
np_mode1=np.ndarray(shape=(2,2), dtype=float, order='F')
print(np_mode1)

# ndarray constructor mode 2
np_mode2=np.ndarray((2,), buffer=np.array([1,2,3]),offset=np.int_().itemsize,dtype=int) # offset = 1*itemsize, i.e. skip first element
print(np_mode2)

# Generate random data according to a normal distribution (mean, stdev, and number of samples)
height=np.round(np.random.normal(1.75,0.2,10),2)
print("height:",type(height))
print(height)
weight=np.round(np.random.normal(60.32,15,10),2)
print("weight:",type(weight))
print(weight)
np_city=np.column_stack((height,weight))
print("np_city:",type(np_city))
print(np_city)
np_city2=np.array((height,weight))
print("np_city2:",type(np_city2))
print(np_city2)

print ("=> End of program")
