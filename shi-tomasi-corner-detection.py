import cv2
import numpy as np

img = cv2.imread('images/pic1.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = np.int0(cv2.goodFeaturesToTrack(gray_img, 200, 0.01, 10))

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Final', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
