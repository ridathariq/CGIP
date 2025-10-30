import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    x, y = 0, r
    d = 3 - 2*r
    points = []

    while x <= y:
        points += [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x), 
            (xc - y, yc + x),
            (xc + y, yc - x), 
            (xc - y, yc - x)
        ]
        if d < 0:
            d += 4*x + 6
        else:
            d += 4*(x - y) + 10
            y -= 1
        x += 1

    return points

# Draw the circle
circle = bresenham_circle(0, 0, 50)
plt.plot(*zip(*circle), 'bo') 
plt.gca().set_aspect('equal')
plt.show()
