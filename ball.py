import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')

radius = 0.3
x, y = radius, 5.5
vx, vy = 0.02, 0.0
g = -0.015
bounce_loss = 0.85

ball = plt.Circle((x, y), radius, color='purple')
ax.add_patch(ball)

def update(frame):
    global x, y, vx, vy
    x += vx
    vy += g
    y += vy
    if y < radius:
        y = radius
        vy = -vy * bounce_loss
    if x > 10 - radius:
        x = 10 - radius
        vx = vy = 0
    ball.center = (x, y)
    return (ball,)

ani = FuncAnimation(fig, update, frames=range(800), interval=30, blit=True)
plt.show()
