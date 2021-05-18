import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/messi5.jpg', cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(img, 100, 200)

titles = ['Image', 'Canny']
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
