import reaction_diffusion_by_explicit as expl
import reaction_diffusion_by_implicit as impl
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

n = 20
def exact_solution(N=n, t=200, deltat=0.01, deltax=2*np.pi/n, D=1):
    x = np.zeros((N, t))
    for i in range(t):
        x[:, i] = np.exp(-deltat*D*i) * np.sin(np.linspace(0, 2*np.pi, N))
    return x


x1 = expl.explicit_test(N=n, t=200, deltat=0.01, deltax=2*np.pi/n, D=1)
x2 = impl.implicit_test(N=n, t=200, deltat=0.01, deltax=2*np.pi/n, D=1)
x3 = exact_solution()

def update(i):
    global x1, x2, x3
    plt.cla()
    plt.plot(x1[:, i], 'r')
    plt.plot(x2[:, i], 'b')
    plt.plot(x3[:, i], 'g')

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, interval=100, frames=200)
plt.show()
