# Аппроксимация функции

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def f(x):
    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)
A = np.array([[1,1], [1,4]])
b = [f(1),f(15)]
z = np.linalg.solve(A, b)
print (z)

def f1(x):
    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)
A = np.array([[1,1,1], [1,4,16], [1,10,100]])
b = [f(1),f(8),f(15)]
z1 = np.linalg.solve(A, b)
print (z1)

def f2(x):
    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)
A = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = [f(1),f(4),f(10),f(15)]
z2 = np.linalg.solve(A, b)
print (z2)

%matplotlib inline
from matplotlib import pylab as plt
x = np.arange(1, 15, 0.1)
y = f2(x)
plt.plot (x, y)
plt.show

# [ 4.36264154 -1.29552587  0.19333685 -0.00823565]
