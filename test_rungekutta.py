import numpy as np
import matplotlib.pyplot as plt
from rungekutta import rungekutta

def rosenzwig_macarthur(x, t):
    k = 3
    a = 1
    mu = 3
    D = 1
    r = 1
    next_x = r*x[0]*(1 - x[0]/k) - x[0]*x[1]/(a + x[0])
    next_y = x[1]*(mu*x[0]/(a+x[0])-D)
    return np.array([next_x, next_y])


loops = 100
x = np.zeros((loops+1, 2))

#parameters
deltat = 0.5

#initial value
x[0][0] = 1
x[0][1] = 1
for i in range(loops):
    x[i+1] = rungekutta(rosenzwig_macarthur, x[i], i, deltat)
t = np.linspace(0, loops+1, loops+1)

plt.plot(t, x[:,0])
plt.plot(t, x[:,1])
plt.show()

