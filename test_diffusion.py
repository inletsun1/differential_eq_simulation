import reaction_diffusion_by_explicit as expl
import reaction_diffusion_by_implicit as impl
import matplotlib.animation as animation
import matplotlib.pyplot as plt

x1 = expl.explicit_test(t=200)
x2 = impl.implicit_test(t=200)

def update(i):
    global x1, x2
    plt.cla()
    plt.plot(x1[:, i], 'r')
    plt.plot(x2[:, i], 'b')

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, interval=10, frames=200)
plt.show()
