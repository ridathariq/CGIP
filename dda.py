import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    steps = max(abs(dx), abs(dy))   
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


# Example usage
x1, y1 = 10, 50
x2, y2 = 90, 50

x_coords, y_coords = dda_line(x1, y1, x2, y2)


plt.plot(x_coords, y_coords,'ko') 
plt.axis("equal")
plt.show()
