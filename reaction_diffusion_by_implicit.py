import numpy as np
import sys

def implicit_test(N=100, t=200, deltat=0.05, deltax=1):
    #parameters
    D = 0.5
    theta = 0.5
    #descretization

    #mesh size
    r = D*deltat/(deltax**2)

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

    inv_diffuse = np.linalg.inv(diffuse)


    #initial values
    x = np.zeros((N, t))
    x[int(N/2), 0] = 1

    #simulate by explicit method
    for i in range(0, t-1):
        x[:, i+1] = inv_diffuse.dot(x[:, i])
        
    return x

