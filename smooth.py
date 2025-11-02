import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)

# Linear Filters
average_filtered = cv2.blur(image, (3,3))
gaussian_filtered = cv2.GaussianBlur(image, (5,5), 0)
box_filtered = cv2.boxFilter(image, -1, (3,3), normalize=True)


median_filtered = cv2.medianBlur(image, 3)
kernel = np.ones((3,3), np.uint8)
min_filtered = cv2.erode(image, kernel)
max_filtered = cv2.dilate(image, kernel)


bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)

titles = [
    'Original', 'Average', 'Gaussian', 'Box Filter',
    'Median', 'Min', 'Max', 'Bilateral'
]
images = [
    image, average_filtered, gaussian_filtered, box_filtered,
    median_filtered, min_filtered, max_filtered, bilateral_filtered
]

plt.figure(figsize=(14,10))
for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()

plt.show()
