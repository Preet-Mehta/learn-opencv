import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg', -1)
cv2.imshow('Image', img)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.xticks([]), plt.yticks([])  # Hides the coordinates.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
