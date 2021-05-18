import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('images/messi5.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

lap = np.uint8(np.absolute(lap))
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
canny = cv2.Canny(img, 100, 200)
sobel_both = cv2.bitwise_or(sobel_x, sobel_y)

titles = ['Image', 'Lap', 'Sobel_X', 'Sobel_Y', 'Sobel', 'Canny']
images = [img, lap, sobel_x, sobel_y, sobel_both, canny]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
