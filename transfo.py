import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('img.png.jpg', cv2.IMREAD_GRAYSCALE)

# ---------------------------
# 1. Linear Transformations
# ---------------------------

# Identity Transformation (output = input)
identity = image.copy()

# Negative Transformation (output = 255 - input)
negative = 255 - image

# ---------------------------
# 2. Logarithmic Transformations
# ---------------------------

# Log Transformation: s = c * log(1 + r)
c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image.astype(np.float32))
log_transformed = np.uint8(log_transformed)

# Inverse-Log Transformation: s = c * (exp(r) - 1)
c = 255 / (np.exp(1) - 1)
inv_log_transformed = c * (np.exp(image / 255.0) - 1)
inv_log_transformed = np.uint8(inv_log_transformed * 255 / np.max(inv_log_transformed))

# ---------------------------
# 3. Power-Law (Gamma) Transformations
# ---------------------------

# nth Power Transformation (gamma > 1 -> darkens)
gamma = 2.0
power_transformed = np.array(255 * ((image / 255) ** gamma), dtype='uint8')

# nth Root Transformation (gamma < 1 -> brightens)
gamma = 0.5  # 1/2
root_transformed = np.array(255 * ((image / 255) ** gamma), dtype='uint8')

# ---------------------------
# 4. Display Results
# ---------------------------
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