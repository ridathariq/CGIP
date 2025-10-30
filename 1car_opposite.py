

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

# First car (moving left to right)
body1 = plt.Rectangle((10, 60), width=60, height=20, fill=False, edgecolor='black', linewidth=2)
wheel1_1 = plt.Circle((20, 52), radius=4, facecolor='black')
wheel1_2 = plt.Circle((50, 52), radius=4, facecolor='black')

# Second car (moving right to left)
body2 = plt.Rectangle((150, 30), width=60, height=20, fill=False, edgecolor='blue', linewidth=2)
wheel2_1 = plt.Circle((160, 22), radius=4, facecolor='black')
wheel2_2 = plt.Circle((190, 22), radius=4, facecolor='black')

# Add all parts to plot
ax.add_patch(body1)
ax.add_patch(wheel1_1)
ax.add_patch(wheel1_2)
ax.add_patch(body2)
ax.add_patch(wheel2_1)
ax.add_patch(wheel2_2)

def update(frame):
    # First car moves right (left to right)
    x_offset1 = frame * 2  
    body1.set_xy((10 + x_offset1, 60))
    wheel1_1.set_center((20 + x_offset1, 52))
    wheel1_2.set_center((50 + x_offset1, 52))

    # Second car moves left (right to left)
    x_offset2 = frame * -2  # Negative value for opposite direction
    body2.set_xy((150 + x_offset2, 30))
    wheel2_1.set_center((160 + x_offset2, 22))
    wheel2_2.set_center((190 + x_offset2, 22))
    
    return body1, wheel1_1, wheel1_2, body2, wheel2_1, wheel2_2

ani = FuncAnimation(fig, update, frames=range(0, 120), interval=50, blit=True, repeat=True)
plt.show()