import numpy as np
import matplotlib.pyplot as plt
from rungekutta import rungekutta
from euler_method import euler_method

ka = 3.3; ki = 2.8; gammaa = 0.2; gammai = 0.1; thetaa = 10**(-3); thetai = 10**(-3);
Rtot = 2.0; kA = 3.0; kI = 1.6; KA = 0.44; KI = 0.01; 
def ultrasensitive_LEGI(x, t):
    next_a = ka*s[i]-gammaa*x[0]+thetaa
    next_i = ki*s[i]-gammai*x[1]+thetai
    next_r = x[0]*(kA*(Rtot-x[2])/(KA + Rtot-x[2])) - x[1]*(kI*x[2]/(KI + x[2]))
    return np.array([next_a, next_i, next_r])


loops = 100000
x = np.zeros((loops+1, 3))
s = np.zeros(loops+1)

#parameters
deltat = 0.001

#initial value
s[int(10/deltat)::] = 1.0
s[int(50/deltat)::] = 0.0
x[0][0] = (ka*s[0] + thetaa)/gammaa
x[0][1] = (ki*s[0] + thetai)/gammai
x[0][2] = 0.0328
for i in range(loops):
    x[i+1] = rungekutta(ultrasensitive_LEGI, x[i], i, deltat)

t = np.linspace(0, loops+1, loops+1)*deltat

fig, ax1 = plt.subplots()
ax1.plot(t, x[:,2], 'r')
ax2 = ax1.twinx()
ax2.plot(t, s, 'g')
plt.ylim(-min(s)*0.1, max(s)*(1.1))

'''
fig2, ax3 = plt.subplots()
ax3.plot(t, x[:,0])
ax3.plot(t, x[:,1])

#error test
test = np.zeros((loops+1, 2))
#test[:, 0] = (x[:, 0]*kA)*(Rtot-x[:, 2])/(KA + (Rtot-x[:, 2]))
test[:, 0] = (x[:, 0]*kA)*(Rtot-x[:, 2])
#test[:, 1] = (x[:, 1]*kI)*x[:, 2]/(KI + x[:, 2])
test[:, 1] = (x[:, 1]*kI)*x[:, 2]
fig3, ax4 = plt.subplots()
ax4.plot(test[:, 0])
fig4, ax5 = plt.subplots()
ax5.plot(test[:, 1])
'''
plt.show()
