import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

#parameters
D = 0.5
#descretization

#mesh size
N = 100
t = 200
theta = 0.5

deltat = 0.05
deltax = 1
r = D*deltat/(deltax**2)
print("r = " + str(r))
if r>0.5:
    print("This scheme is unstable!! The program has been stopped.")
    sys.exit()
#equation
def func(x):
    return 0

#boundary condition
diffuse = (1+2*r*theta)*np.eye(N, k=0) - r*theta*np.eye(N, k=1) - r*theta*np.eye(N, k=-1)
#Dirichlet condition
#Neumann condition
#periodic boundary condition
diffuse[0,-1] = -r*theta
diffuse[-1,0] = -r*theta
print(diffuse)

inv_diffuse = np.linalg.inv(diffuse)


#initial values
x = np.zeros((N, t))
x[int(N/2), 0] = 1

#simulate by explicit method
fig = plt.figure()
ims = []
for i in range(0, t-1):
    x[:, i+1] = inv_diffuse.dot(x[:, i])
    im = plt.plot(x[:, i+1], 'b')
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
