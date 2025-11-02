import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)


identity = image.copy()


negative = 255 - image


c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image.astype(np.float32))
log_transformed = np.uint8(log_transformed)


c = 255 / (np.exp(1) - 1)
inv_log_transformed = c * (np.exp(image / 255.0) - 1)
inv_log_transformed = np.uint8(inv_log_transformed * 255 / np.max(inv_log_transformed))



gamma = 2.0
power_transformed = np.array(255 * ((image / 255) ** gamma), dtype='uint8')

gamma = 0.5  
root_transformed = np.array(255 * ((image / 255) ** gamma), dtype='uint8')


titles = [
    'Original Image', 'Identity Transformation', 'Negative Transformation',
    'Log Transformation', 'Inverse Log Transformation',
    'Power (Gamma>1)', 'Root (Gamma<1)'
]

images = [
    image, identity, negative,
    log_transformed, inv_log_transformed,
    power_transformed, root_transformed
]

plt.figure(figsize=(14, 10))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()

plt.show()
