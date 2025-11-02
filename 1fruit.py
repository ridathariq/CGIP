

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


tree_trunk = plt.Line2D([5, 5], [0, 4], color='brown', linewidth=3)
tree_top = plt.Circle((5, 6), 2, color='green', alpha=0.5)


fruit = plt.Circle((5, 7), 0.3, color='red')

ax.add_line(tree_trunk)
ax.add_patch(tree_top)
ax.add_patch(fruit)

def update(frame):
    if frame < 20:
        fruit_y = 7  
    else:
        
        fruit_y = 7 - (frame - 20) * 0.1
    
    fruit.center = (5, fruit_y)
    return fruit,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
