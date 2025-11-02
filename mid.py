import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x, y = 0, r
    d = 1 - r
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
            d += 2*x + 3
        else:
            d += 2*(x - y) + 5
            y -= 1
        x += 1

    return points


xc, yc = 0, 0
radius = 50
circle_points = midpoint_circle(xc, yc, radius)

plt.plot(*zip(*circle_points), 'bo') 
plt.gca().set_aspect('equal')
plt.show()

