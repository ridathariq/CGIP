import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = 2*dy - dx

    x, y = x1, y1
    x_coords = [x]
    y_coords = [y]

    for _ in range(dx):
        x += 1
        if p < 0:
            p = p + 2*dy
        else:
            y += 1
            p = p + 2*(dy - dx)
        x_coords.append(x)
        y_coords.append(y)

    return x_coords, y_coords

x1, y1 = 10, 60
x2, y2 = 90, 60
x_coords, y_coords = bresenham(x1, y1, x2, y2)

plt.plot(x_coords, y_coords, 'ko')
plt.axis("equal")
plt.show()