import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)
sobel_magnitude = np.uint8(np.clip(sobel_magnitude, 0, 255))

prewitt_x = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewitt_y = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
prewitt_x_img = cv2.filter2D(image, -1, prewitt_x)
prewitt_y_img = cv2.filter2D(image, -1, prewitt_y)
prewitt_magnitude = cv2.magnitude(prewitt_x_img.astype(float), prewitt_y_img.astype(float))
prewitt_magnitude = np.uint8(np.clip(prewitt_magnitude, 0, 255))

roberts_x = np.array([[1, 0],[0, -1]])
roberts_y = np.array([[0, 1],[-1, 0]])
roberts_x_img = cv2.filter2D(image, -1, roberts_x)
roberts_y_img = cv2.filter2D(image, -1, roberts_y)
roberts_magnitude = cv2.magnitude(roberts_x_img.astype(float), roberts_y_img.astype(float))
roberts_magnitude = np.uint8(np.clip(roberts_magnitude, 0, 255))

sobel_sharpened = cv2.addWeighted(image, 1.0, sobel_magnitude, 0.5, 0)
prewitt_sharpened = cv2.addWeighted(image, 1.0, prewitt_magnitude, 0.5, 0)
roberts_sharpened = cv2.addWeighted(image, 1.0, roberts_magnitude, 0.5, 0)

titles = [
    'Original Image',
    'Sobel Edge', 'Sobel Sharpened',
    'Prewitt Edge', 'Prewitt Sharpened',
    'Roberts Edge', 'Roberts Sharpened'
]

images = [
    image,
    sobel_magnitude, sobel_sharpened,
    prewitt_magnitude, prewitt_sharpened,
    roberts_magnitude, roberts_sharpened
]

plt.figure(figsize=(14,10))
for i in range(len(images)):
    plt.subplot(4, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()