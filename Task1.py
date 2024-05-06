import numpy as np
import matplotlib.pyplot as pp
import os

x = np.linspace(-5,5,201)
y = -20*np.exp(-0.2*np.sqrt(0.5*x**2))-np.exp(0.5*(np.cos(2*np.pi*x)+1))+np.e+20
fig, ax = pp.subplots()
ax.set_xlim(-5,5)
ax.set_ylabel("f(x)")
ax.set_xlabel("x")
ax.plot(x, y)
pp.show()
try:
 os.mkdir("results")
except:
    pass
f = open("results\\res.csv", "x")
for i in range(len(x)):
    f.write("{i},{x},{f}\n".format(i=i,x=x[i],f=y[i]))
f.close()
