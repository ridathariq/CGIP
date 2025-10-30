import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



fig,ax = plt.subplots()
ax.set_xlim(0,12)
ax.set_ylim(0,12)

hill1 = plt.Polygon([[0, 0], [3, 0], [1.5, 2]], color = 'green')
hill2 = plt.Polygon([[6, 0], [10, 0], [7, 8]], color = 'green')
sun = plt.Circle((3,-1), radius = 1, color = 'red')



ax.add_patch(hill1)
ax.add_patch(hill2)
ax.add_patch(sun)

def update(frame):
    sun_y =-1 + frame * 0.05
    sun.center = (3, sun_y)
    return (sun,)

ani = FuncAnimation(fig, update, frames=range(200), interval = 30, blit = True)
plt.show()