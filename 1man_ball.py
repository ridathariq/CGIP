

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

man_head = plt.Circle((2, 5), 0.3, color='black')
man_body = plt.Line2D([2, 2], [4.7, 3], color='black', linewidth=2)
man_hand = plt.Line2D([2, 3], [4, 4], color='black', linewidth=2)

ball = plt.Circle((3.2, 4), 0.3, color='red')

ax.add_patch(man_head)
ax.add_line(man_body)
ax.add_line(man_hand)
ax.add_patch(ball)

def update(frame):
    x_pos = 2 + frame * 0.05
    
    man_head.center = (x_pos, 5)
    man_body.set_data([x_pos, x_pos], [4.7, 3])
    man_hand.set_data([x_pos, x_pos + 1], [4, 4])
    ball.center = (x_pos + 1.2, 4)
    
    return man_head, man_body, man_hand, ball

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()