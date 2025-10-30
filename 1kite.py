import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

head = plt.Circle((2, 5), 0.3, color='black')
body = plt.Line2D([2, 2], [4.7, 3], color='black', linewidth=2)
hand = plt.Line2D([2, 3], [4, 4.5], color='black', linewidth=2)

kite, = ax.plot(6, 8, 's', color='red', markersize=15)

string, = ax.plot([3, 6], [4.5, 8], 'black')

ax.add_patch(head)
ax.add_line(body)
ax.add_line(hand)

def update(frame):
    
    kite_y = 8 + 0.5 * frame * 0.1
    kite.set_data([6], [kite_y])
    string.set_data([3, 6], [4.5, kite_y])
    return head, body, hand, kite, string

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()