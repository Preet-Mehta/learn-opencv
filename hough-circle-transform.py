import cv2
import numpy as np

img = cv2.imread('images/smarties.png')
final = img.copy()
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img, 5)

circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for circle in circles[0, :]:
    x, y, r = circle
    cv2.circle(final, (x, y), r, (0, 0, 0), 2)
    cv2.circle(final, (x, y), 1, (0, 0, 0), 2)

cv2.imshow('Final Image', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
