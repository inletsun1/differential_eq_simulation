import numpy as np

def implicit_test(N=100, t=200, deltat=0.4, deltax=1, D=1):
    #parameters
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
    x[:,0] = np.sin(np.linspace(0, 2*np.pi, N))

    #simulate by explicit method
    for i in range(0, t-1):
        x[:, i+1] = inv_diffuse.dot(x[:, i])
        
    return x

