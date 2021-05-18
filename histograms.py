import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg', 0)
# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (0, 0), (200, 100), 255, -1)
# cv2.rectangle(img, (0, 0), (100, 100), 127, -1)

# b, g, r = cv2.split(img)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
plt.plot(hist)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
