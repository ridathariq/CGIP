import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image in grayscale
image = cv2.imread("img.png.jpg", cv2.IMREAD_GRAYSCALE)

# Define threshold values
lower_threshold = 100
upper_threshold = 160

# Create an empty image for the result
threshold_image = np.zeros_like(image)

# Apply two-level thresholding
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i, j] > upper_threshold:
            threshold_image[i, j] = 255
        elif lower_threshold < image[i, j] <= upper_threshold:
            threshold_image[i, j] = 255
        else:
            threshold_image[i, j] = 0

# Display the original and thresholded images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Two Threshold Image')
plt.imshow(threshold_image, cmap='gray')

plt.show()
