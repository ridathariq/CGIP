

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

hill1 = plt.Polygon([[0, 0], [3, 0], [1.5, 2]], color='green')
hill2 = plt.Polygon([[7, 0], [10, 0], [8.5, 3]], color='green')

sun = plt.Circle((5, -1), 0.5, color='yellow')

ax.add_patch(hill1)
ax.add_patch(hill2)
ax.add_patch(sun)

def update(frame):
    sun_y = -1 + frame * 0.05
    sun.center = (5, sun_y)
    return (sun,)

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()