
import numpy as np
import matplotlib.pyplot as plt
import math

def translate(points, tx, ty):
    return points + [tx, ty]

def scale(points, sx, sy):
    return points * [sx, sy]

def rotate(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    rot = [[math.cos(angle_rad), -math.sin(angle_rad)],
           [math.sin(angle_rad),  math.cos(angle_rad)]]
    return points @ np.array(rot).T

def reflect(points, axis='x'):
    if axis == 'x':
        mat = [[1, 0], [0, -1]]
    elif axis == 'y':
        mat = [[-1, 0], [0, 1]]
    else:
        mat = [[-1, 0], [0, -1]]
    return points @ np.array(mat).T


def plot_shapes(original, transformed, label):

    orig_x = np.append(original[:,0], original[0,0])
    orig_y = np.append(original[:,1], original[0,1])
    trans_x = np.append(transformed[:,0], transformed[0,0])
    trans_y = np.append(transformed[:,1], transformed[0,1])


    plt.plot(orig_x, orig_y, 'b-', label="Original")
    plt.plot(trans_x, trans_y, 'r-', label=label)
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.show()

triangle = np.array([[1,1],[4,1],[2.5,4]])

print("Choose transformation:")
print("1 - Translation")
print("2 - Scaling")
print("3 - Rotation")
print("4 - Reflection")

choice = input("Enter choice: ")

if choice == '1':
    tx, ty = map(float, input("Enter tx ty: ").split())
    result = translate(triangle, tx, ty)
    plot_shapes(triangle, result, "Translated")

elif choice == '2':
    sx, sy = map(float, input("Enter sx sy: ").split())
    result = scale(triangle, sx, sy)
    plot_shapes(triangle, result, "Scaled")

elif choice == '3':
    angle = float(input("Enter angle in degrees: "))
    result = rotate(triangle, angle)
    plot_shapes(triangle, result, "Rotated")

elif choice == '4':
    axis = input("Enter axis (x, y, origin): ")
    result = reflect(triangle, axis)
    plot_shapes(triangle, result, "Reflected")

else:
    print("Invalid choice!")

