
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.set_aspect('equal')


body = plt.Rectangle((10, 50), width=80, height=30, fill=False, edgecolor='black', linewidth=2)
wheel1 = plt.Circle((25, 40), radius=5, facecolor='black')
wheel2 = plt.Circle((75, 40), radius=5, facecolor='black')

ax.add_patch(body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

def update(frame):
  
    x_offset = frame * 2  

    body.set_xy((10 + x_offset, 50))
    wheel1.set_center((25 + x_offset, 40))
    wheel2.set_center((75 + x_offset, 40))

    return body, wheel1, wheel2

ani = FuncAnimation(fig, update, frames=range(0, 120), interval=50, blit=True, repeat=True)

plt.show()

