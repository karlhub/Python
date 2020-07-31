# Use of Python package: Matplotlib - Extended

# Import subpackage "pyplot"
# Documentation in internet: https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
import matplotlib.pyplot as plt
import numpy as np

# Working with multiple figures and axes.
# MATLAB, and pyplot, have the concept of the current figure and the current axes.
# All plotting commands apply to the current axes.
# The function gca() returns the current axes (a matplotlib.axes.Axes instance)
# The function gcf() returns the current figure (matplotlib.figure.Figure instance).
# Normally, you don't have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

i=0.0
while True:
    print("i:",i,"Exp(",-i,"):",np.exp(-i),"cos(",2*np.pi*i,"):",np.cos(2*np.pi*i))
    i=i+0.1
    if i>5.0:
        break

print()
print("cos(pi):",np.cos(np.pi))
print("cos(2pi):",np.cos(2*np.pi))
print("cos(10pi):",np.cos(10*np.pi))

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

print ("=> End of program")
