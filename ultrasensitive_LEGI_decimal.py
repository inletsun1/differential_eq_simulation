import numpy as np
import matplotlib.pyplot as plt
from rungekutta import rungekutta
from euler_method import euler_method
from decimal import Decimal, getcontext, FloatOperation

getcontext().traps[FloatOperation] = True
#getcontext().prec = 100
ka = Decimal("3.3"); ki = Decimal("2.8"); gammaa = Decimal("0.2"); gammai = Decimal("0.1"); 
thetaa = Decimal("0.001"); thetai = Decimal("0.001");
Rtot = Decimal("2.0"); kA = Decimal("3.0"); kI = Decimal("1.6"); KA = Decimal("0.44"); KI = Decimal("0.01"); 
def ultrasensitive_LEGI(x, t):
    #next_s = 0
    next_a = ka*s[i]-gammaa*x[0]+thetaa
    next_i = ki*s[i]-gammai*x[1]+thetai
    next_r = (x[0]*kA)*(Rtot-x[2])/(KA + (Rtot-x[2])) - (x[1]*kI)*x[2]/(KI + x[2])
    #next_r = (x[0]*kA)/(KA/(Rtot-x[2]) + 1.0) - (x[1]*kI)*x[2]/(KI + x[2])
    #plt.plot(t, (x[0]*kA)*(Rtot-x[2])/(KA + (Rtot-x[2])), 'o')
    #plt.plot(t, (x[0]*kA)*(Rtot-x[2]), 'o')
    #plt.plot(t, (KA + (Rtot-x[2])), 'o')
    #plt.plot(t, (x[1]*kI)*x[2]/(KI + x[2]), 'o')
    #plt.plot(t, (x[1]*kI)*x[2], 'o')
    #plt.plot(t, (KI + x[2]), 'o')

    return np.array([next_a, next_i, next_r])


loops = 100000
x = np.zeros((loops+1, 3), dtype=Decimal)
s = np.zeros(loops+1, dtype=Decimal)

#parameters
deltat = Decimal("0.001")

#initial value
s[int(10/deltat)::] = Decimal("1.0")
#s[int(180/deltat)::] = Decimal("0.0")
x[0][0] = (ka*s[0] + thetaa)/gammaa
x[0][1] = (ki*s[0] + thetai)/gammai
x[0][2] = Decimal("0.0328")
for i in range(loops):
    x[i+1] = rungekutta(ultrasensitive_LEGI, x[i], i, deltat)
    
#t = np.linspace(0, loops+1, loops+1, dtype=Decimal)*deltat
fig, ax1 = plt.subplots()
#ax1.plot(t, x[:,2], 'r')
ax1.plot(x[:,2], 'r')
ax2 = ax1.twinx()
#ax2.plot(t, s, 'g')
ax2.plot(s, 'g')
#plt.ylim(-min(s)*Decimal("0.1"), max(s)*Decimal("1.1"))

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
