import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((5, 5), np.uint8)
img = cv2.imread('images/smarties.png', cv2.IMREAD_GRAYSCALE)
_, masked = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

dilated = cv2.dilate(masked, kernel, iterations=2)
erosion = cv2.erode(masked, kernel, iterations=2)
opening = cv2.morphologyEx(masked, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(masked, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(masked, cv2.MORPH_GRADIENT, kernel)
bh = cv2.morphologyEx(masked, cv2.MORPH_BLACKHAT, kernel)

titles = ['Image', 'Masked', 'Dilated', 'Erosion', 'Open', 'Close', 'Gradient', 'BH']
images = [img, masked, dilated, erosion, opening, closing, gradient, bh]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
