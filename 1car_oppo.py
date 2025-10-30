

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

# Start from right side (change initial positions)
body = plt.Rectangle((150, 50), width=80, height=30, fill=False, edgecolor='black', linewidth=2)
wheel1 = plt.Circle((165, 40), radius=5, facecolor='black')
wheel2 = plt.Circle((215, 40), radius=5, facecolor='black')


body2 = plt.Rectangle((30, 50), width=80, height=30, fill=False, edgecolor='black', linewidth=2)
wheel11 = plt.Circle((25, 40), radius=5, facecolor='black')
wheel12 = plt.Circle((75, 40), radius=5, facecolor='black')

ax.add_patch(body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

ax.add_patch(body2)
ax.add_patch(wheel11)
ax.add_patch(wheel12)

def update(frame):
    # Move left by subtracting from x-position
    x_offset = frame * 2  
    body.set_xy((150 - x_offset, 50))
    wheel1.set_center((165 - x_offset, 40))
    wheel2.set_center((215 - x_offset, 40))
    

    x_offset1 = frame * -2  
    body2.set_xy((30 - x_offset1, 50))
    wheel11.set_center((25 - x_offset1, 40))
    wheel12.set_center((75 - x_offset1, 40))
    
    return body, wheel1, wheel2, body2, wheel11, wheel12


ani = FuncAnimation(fig, update, frames=range(0, 120), interval=50, blit=True, repeat=True)


plt.show()