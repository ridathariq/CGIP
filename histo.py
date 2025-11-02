import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)

def contrast_stretching(img):
  
    r_min, r_max = np.min(img), np.max(img)

    stretched = ((img - r_min) / (r_max - r_min)) * 255
    return np.uint8(stretched)

contrast_stretched = contrast_stretching(image)


def histogram_equalization(img):

    hist, _ = np.histogram(img.flatten(), 256, [0, 256])

    pdf = hist / np.sum(hist)
    

    cdf = np.cumsum(pdf)
    

    cdf_normalized = np.uint8(255 * cdf)
    

    equalized = cdf_normalized[img]
    return equalized

hist_equalized = histogram_equalization(image)

# ---------------------------
titles = ['Original Image', 'Contrast Stretched', 'Histogram Equalized']
images = [image, contrast_stretched, hist_equalized]

plt.figure(figsize=(12, 6))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()

plt.show()
