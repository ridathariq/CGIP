import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)

sun = plt.Circle((0, 0), 1, color='yellow')
earth = plt.Circle((5, 0), 0.5, color='blue')

ax.add_patch(sun)
ax.add_patch(earth)

def update(frame):
    angle = frame * 0.1
    earth_x = 5 * np.cos(angle)
    earth_y = 5 * np.sin(angle)
    
    earth.center = (earth_x, earth_y)
    return earth,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()