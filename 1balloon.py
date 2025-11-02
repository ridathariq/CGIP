import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)

b1 = plt.Circle((50, -10), 10, color='red')
ax.add_patch(b1)
b2 = plt.Circle((90, -10), 10, color='blue')
ax.add_patch(b2)

string1, = ax.plot([50, 50], [0, 0], color='black')
string2, = ax.plot([90, 90], [0, 0], color='black')
def update(frame):
    y_pos = -10 + frame * 2  
    

    b1.center = (50, y_pos)
    string1.set_data([50, 50], [0, y_pos - 10])
    b2.center = (90, y_pos)
    string2.set_data([90, 90], [0, y_pos - 10])
    return b1, string1,b2,string2

ani = FuncAnimation(fig, update, frames=100, interval=30, blit=True)

plt.show()
