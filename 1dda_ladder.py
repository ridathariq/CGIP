import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))   
    x_inc = dx / steps              
    y_inc = dy / steps              

    x, y = x1, y1
    x_coords, y_coords = [], []

    for _ in range(steps + 1):      
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc

    return x_coords, y_coords



left_x, right_x = 10, 90     
top_y, bottom_y = 20, 120    
num_rungs = 8                

for (x1, y1, x2, y2) in [(left_x, top_y, left_x, bottom_y),
                         (right_x, top_y, right_x, bottom_y)]:
    x_coords, y_coords = dda_line(x1, y1, x2, y2)
    plt.plot(x_coords, y_coords, 'ko')   

for i in range(num_rungs):
    y = top_y + i * (bottom_y - top_y) / (num_rungs - 1)
    x_coords, y_coords = dda_line(left_x, y, right_x, y)
    plt.plot(x_coords, y_coords, 'ko')


plt.axis("equal")
plt.title("Ladder using DDA Line Algorithm")
plt.gca().invert_yaxis() 
plt.show()

