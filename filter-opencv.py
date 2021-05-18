import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('images/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
res = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
g_blur = cv2.GaussianBlur(img, (5, 5), 0)
m_blur = cv2.medianBlur(img, 5)
b_blur = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Image', '2D Convolution', 'Blur', 'G_Blur', 'M_Blur', 'B_Blur']
images = [img, res, blur, g_blur, m_blur, b_blur]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
