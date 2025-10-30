
import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)

transformations = {
    'Original': image,
    'Identity': image.copy(),
    'Negative': 255 - image,
    'Log': np.uint8(255 * np.log(1 + image) / np.log(256)),
    'Inverse Log': np.uint8(255 * (np.exp(image/255) - 1) / (np.e - 1)),
    'Power (γ=2)': np.uint8(255 * (image/255) ** 2),
    'Root (γ=0.5)': np.uint8(255 * (image/255) ** 0.5)
}

plt.figure(figsize=(14, 8))
for i, (title, img) in enumerate(transformations.items()):
    plt.subplot(2, 4, i+1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()