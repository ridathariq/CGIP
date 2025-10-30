
import numpy as np
import matplotlib.pyplot as plt

# Cube vertices
cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# ------------------- Transformations -------------------
def translate(points, tx, ty, tz):
    return points + [tx, ty, tz]

def scale(points, sx, sy, sz):
    return points * [sx, sy, sz]

def rotate_x(points, angle):
    rad = np.radians(angle)
    rot = [[1, 0, 0],
           [0, np.cos(rad), -np.sin(rad)],
           [0, np.sin(rad),  np.cos(rad)]]
    return points @ np.array(rot).T

def rotate_y(points, angle):
    rad = np.radians(angle)
    rot = [[np.cos(rad), 0, np.sin(rad)],
           [0, 1, 0],
           [-np.sin(rad), 0, np.cos(rad)]]
    return points @ np.array(rot).T

def rotate_z(points, angle):
    rad = np.radians(angle)
    rot = [[np.cos(rad), -np.sin(rad), 0],
           [np.sin(rad),  np.cos(rad), 0],
           [0, 0, 1]]
    return points @ np.array(rot).T

# ------------------- Plot function -------------------
def plot_cube(original, transformed, label):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # edges tell how to connect vertices
    edges = [(0,1),(1,2),(2,3),(3,0),
             (4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]

    # original (blue)
    for a,b in edges:
        ax.plot([original[a,0], original[b,0]],
                [original[a,1], original[b,1]],
                [original[a,2], original[b,2]], "b-")

    # transformed (red)
    for a,b in edges:
        ax.plot([transformed[a,0], transformed[b,0]],
                [transformed[a,1], transformed[b,1]],
                [transformed[a,2], transformed[b,2]], "r-")

    ax.set_title("Blue: Original | Red: " + label)
    plt.show()

# ------------------- Menu -------------------
print("1. Translation\n2. Scaling\n3. Rotation X\n4. Rotation Y\n5. Rotation Z")
choice = input("Enter your choice: ")

if choice == "1":
    tx, ty, tz = map(float, input("Enter tx ty tz: ").split())
    result = translate(cube, tx, ty, tz)
    plot_cube(cube, result, "Translated")

elif choice == "2":
    sx, sy, sz = map(float, input("Enter sx sy sz: ").split())
    result = scale(cube, sx, sy, sz)
    plot_cube(cube, result, "Scaled")

elif choice == "3":
    angle = float(input("Enter angle: "))
    result = rotate_x(cube, angle)
    plot_cube(cube, result, "Rotated X")

elif choice == "4":
    angle = float(input("Enter angle: "))
    result = rotate_y(cube, angle)
    plot_cube(cube, result, "Rotated Y")

elif choice == "5":
    angle = float(input("Enter angle: "))
    result = rotate_z(cube, angle)
    plot_cube(cube, result, "Rotated Z")
