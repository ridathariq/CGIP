import matplotlib.pyplot as plt

def dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps =max(abs(dx),abs(dy))
    x_inc=dx/steps
    y_inc=dy/steps
    x,y = x1,y1
    
    x_coords,y_coords=[],[]
    
    for _ in range(steps+1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x+=x_inc
        y+=y_inc
    return x_coords,y_coords
x1,y1=10,50
x2,y2=90,50
x3,y3=10,100
x4,y4=90,100
x_coords,y_coords=dda(x1,y1,x2,y2)
plt.plot(x_coords,y_coords,'ko')
x_coords,y_coords=dda(x3,y3,x4,y4)
plt.plot(x_coords,y_coords,'ko')
x_coords,y_coords=dda(x1,y1,x3,y3)
plt.plot(x_coords,y_coords,'ko')
x_coords,y_coords=dda(x2,y2,x4,y4)
plt.plot(x_coords,y_coords,'ko')
plt.axis("equal")
plt.show()