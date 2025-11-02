

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def dda_line(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc, y_inc = dx / steps, dy / steps

    x, y = x1, y1
    x_coords, y_coords = [], []

    for _ in range(steps):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc

    return x_coords, y_coords

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.set_aspect('equal')


road_x, road_y = dda_line(0, 40, 200, 40)
ax.plot(road_x, road_y, color='black', linewidth=15)


for i in range(0, 200, 25):
    mark_x, mark_y = dda_line(i, 40, i+12, 40)
    ax.plot(mark_x, mark_y, color='yellow', linewidth=3)


car_body = plt.Rectangle((10, 45), width=40, height=15, facecolor='blue')
wheel1 = plt.Circle((20, 42), radius=5, facecolor='black')
wheel2 = plt.Circle((40, 42), radius=5, facecolor='black')

ax.add_patch(car_body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

def update(frame):

    x_offset = frame * 2
    car_body.set_xy((10 + x_offset, 45))
    wheel1.set_center((20 + x_offset, 42))
    wheel2.set_center((40 + x_offset, 42))
    
    return car_body, wheel1, wheel2

ani = FuncAnimation(fig, update, frames=range(0, 80), interval=50, blit=True, repeat=True)

plt.show()
