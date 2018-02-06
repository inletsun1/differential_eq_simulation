import numpy as np
import matplotlib.pyplot as plt
import sys

#descretization

#mesh size
N = 100
t = 500
deltat = 0.01
deltax = 1
r = deltat/(deltax**2)
print("r = " + str(r))
if r>0.5:
    print("This scheme is unstable!! The program has been stopped.")
    sys.exit()
#equation
def func(x):
    return 0

#boundary condition
diffuse = (1-2*r)*np.eye(N, k=0) + r*np.eye(N, k=1) + r*np.eye(N, k=-1)
#Dirichlet condition
#Neumann condition
#periodic boundary condition
diffuse[0,-1] = r
diffuse[-1,0] = r

#initial values
x = np.zeros((N, t))
x[N/2, 0] = 1
#simulate
for i in range(0, t-1):
    x[:, i+1] = diffuse.dot(x[:, i])

plt.plot(x[:, 0])
plt.plot(x[:, -1])
plt.show()
