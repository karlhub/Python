# Use of Python package: Matplotlib
#   1) Type pip3 install matplotlib to install package Matplotlib (data visualizing)
#   2) Type pip3 list to know the packages installed so far.

# Import subpackage "pyplot"
# Documentation in internet: https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
import matplotlib.pyplot as plt

year=[1950,1970,1990,2010]
print("Year:")
print(year)
pop=[2.519,3.692,5.263,6.972]
print("World population (billions):")
print(pop)

# Plot with line between data points
plt.plot(year,pop,"ro")
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.axis([1940,2020,0.0,8.0])
plt.show()

# Plot with only data points not connected between them
plt.scatter(year,pop)
plt.show()

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Plotting with keyword strings
data = {'a': np.arange(4),
        'c': np.random.randint(0, 100, 4),
        'd': np.random.randn(4)}
print(data)
data['b'] = data['a'] + 10 * np.random.randn(4)
print(data)
data['d'] = np.abs(data['d']) * 100
print(data)

plt.scatter('a', 'b', c='c', s='d', data=data) # c: colour? s:size?
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

# Plotting with categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(12, 3))

plt.subplot(141)
plt.bar(names, values)
plt.subplot(142)
plt.scatter(names, values)
plt.subplot(143)
plt.plot(names, values,c='c',linewidth=1.0)
plt.subplot(144)
plt.bar(names, values,color='r')
plt.suptitle('Categorical Plotting')
plt.show()

# Controlling line properties
x1=5
y1=10
x2=25
y2=25
line1,line2=plt.plot(x1,y1,x2,y2,'-',linewidth=2.0,c="r")
line, = plt.plot(x1, y1, '-')
line.set_antialiased(False) # turn off antialiasing

lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.plot([6,8,10],[8,7,10])
plt.show()
# To get a list of settable line properties, call the setp() function with a line or lines as argument
lines = plt.plot([1, 2, 3])
plt.setp(lines)

print ("=> End of program")
