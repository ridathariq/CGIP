
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

# Draw road using DDA
road_x, road_y = dda_line(0, 30, 200, 30)
ax.plot(road_x, road_y, color='gray', linewidth=20)

# Draw road markings using DDA
for i in range(0, 200, 30):
    mark_x, mark_y = dda_line(i, 30, i+15, 30)
    ax.plot(mark_x, mark_y, color='white', linewidth=3)

# Draw hills using DDA
hill1_x, hill1_y = dda_line(0, 50, 80, 80)
hill2_x, hill2_y = dda_line(80, 80, 160, 50)
hill3_x, hill3_y = dda_line(120, 50, 200, 70)

ax.plot(hill1_x, hill1_y, color='green', linewidth=4)
ax.plot(hill2_x, hill2_y, color='darkgreen', linewidth=4)
ax.plot(hill3_x, hill3_y, color='green', linewidth=4)

# Car
car_body = plt.Rectangle((10, 35), width=30, height=10, facecolor='red')
wheel1 = plt.Circle((15, 30), radius=4, facecolor='black')
wheel2 = plt.Circle((35, 30), radius=4, facecolor='black')

ax.add_patch(car_body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

def update(frame):
    # Move car
    x_offset = frame * 2
    car_body.set_xy((10 + x_offset, 35))
    wheel1.set_center((15 + x_offset, 30))
    wheel2.set_center((35 + x_offset, 30))
    
    return car_body, wheel1, wheel2

ani = FuncAnimation(fig, update, frames=range(0, 80), interval=50, blit=True, repeat=True)
plt.show()