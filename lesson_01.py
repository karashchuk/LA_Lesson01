#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
def func(k,x):
    return np.cos(k*x)
x = np.linspace(0,4*np.pi,101)
plt.plot(x,func(1,x), marker="D")
plt.plot(x,func(1.5,x), marker="o")
plt.plot(x,func(2,x), marker=">")