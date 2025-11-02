import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


g = 9.81           
dt = 0.03         
t_max = 5        
t = np.arange(0, t_max, dt)

y0 = 8.0
x_coconut = 5.5      
y_coconut = y0 - 0.5 * g * t**2  

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_facecolor('skyblue')


tree_trunk = plt.Rectangle((4.8, 0), 0.4, 6, color='sienna')
ax.add_patch(tree_trunk)


coconut_radius = 0.3
coconut = plt.Circle((x_coconut, y0), coconut_radius, color='brown')
ax.add_patch(coconut)


def animate(i):
    y = y_coconut[i]
    if y < 0:   
        y = 0
    coconut.center = (x_coconut, y) 
    return coconut,


ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)

plt.show()

