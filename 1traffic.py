import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)
ax.set_aspect('equal')

traffic=plt.Rectangle((80,100),height=50,width=20,linewidth=2,color='black')
ax.add_patch(traffic)

light=plt.Circle((90,125),7,color='red')
ax.add_patch(light)
body = plt.Rectangle((10, 50), width=40, height=20, fill=False, edgecolor='black', linewidth=2)
wheel1 = plt.Circle((16, 40), radius=5, facecolor='black')
wheel2 = plt.Circle((30, 40), radius=5, facecolor='black')

ax.add_patch(body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

def update(frame):
    if frame>30:
        light.set_color('green')
        x = 10 + (frame - 30) * 2  
    else:
        light.set_color('red')
        x = 10  
    body.set_xy((x,50))
    wheel1.center=(16+x,40)
    wheel2.center=(30+x,40)
    return (body,wheel1,wheel2,light)

ani=FuncAnimation(fig,update,frames=100,interval=50,blit=True)
plt.show()