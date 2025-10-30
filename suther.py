import matplotlib.pyplot as plt

# Region codes
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1, code2 = compute_code(x1, y1, xmin, ymin, xmax, ymax), compute_code(x2, y2, xmin, ymin, xmax, ymax)
    while True:
        if not (code1 | code2):   # both inside
            return x1, y1, x2, y2
        elif code1 & code2:       # both outside same region
            return None
        else:
            code_out = code1 or code2
            if code_out & TOP:
                x, y = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax
            elif code_out & BOTTOM:
                x, y = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin
            elif code_out & RIGHT:
                y, x = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1), xmax
            elif code_out & LEFT:
                y, x = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1), xmin

            if code_out == code1:
                x1, y1, code1 = x, y, compute_code(x, y, xmin, ymin, xmax, ymax)
            else:
                x2, y2, code2 = x, y, compute_code(x, y, xmin, ymin, xmax, ymax)

# ---------------- Example -----------------
xmin, ymin, xmax, ymax = 1, 1, 8, 6
x1, y1, x2, y2 = 0, 5, 10, 2

clipped = cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k-', label="Clipping Window")
plt.plot([x1, x2], [y1, y2], 'r--', label="Original Line")

if clipped:
    cx1, cy1, cx2, cy2 = clipped
    plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label="Clipped Line")

plt.legend()
plt.title("Cohen–Sutherland Line Clipping (Simplified)")
plt.grid(True)
plt.show()
