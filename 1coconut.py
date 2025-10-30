import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
g = 9.81             # acceleration due to gravity (m/s^2)
dt = 0.03           # time step
t_max = 5           # total simulation time
t = np.arange(0, t_max, dt)

# Initial position of coconut
y0 = 8.0
x_coconut = 5.5       # x-position of coconut (fixed)
y_coconut = y0 - 0.5 * g * t**2  # s = ut + 0.5gt^2, u=0

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_facecolor('skyblue')

# Draw tree trunk
tree_trunk = plt.Rectangle((4.8, 0), 0.4, 6, color='sienna')
ax.add_patch(tree_trunk)

# Draw coconut as a circle patch
coconut_radius = 0.3
coconut = plt.Circle((x_coconut, y0), coconut_radius, color='brown')
ax.add_patch(coconut)

# Animation function
def animate(i):
    y = y_coconut[i]
    if y < 0:   # stop at ground
        y = 0
    coconut.center = (x_coconut, y)  # move the circle
    return coconut,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)

plt.show()
