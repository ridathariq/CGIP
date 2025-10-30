import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plane, = ax.plot([1, 9], [8, 2], 'brown', linewidth=3)
ball = plt.Circle((2, 7.2), 0.4, color='red')
ax.add_patch(ball)

def update(frame):
    
    ball_x = 2 + frame * 0.1
    ball_y = 8 - frame * 0.08  
    
    ball.center = (ball_x, ball_y)
    return ball,

ani = FuncAnimation(fig, update, frames=80, interval=50, blit=True)
plt.show()