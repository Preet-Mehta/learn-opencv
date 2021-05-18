import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img2 = np.zeros((250, 500, 3), np.uint8)
img3 = cv2.imread("images/messi5.jpg")

img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)

and_op = cv2.bitwise_and(img1, img2)
or_op = cv2.bitwise_or(img1, img2)
xor_op = cv2.bitwise_xor(img1, img2)
not_op = cv2.bitwise_not(img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
# cv2.imshow("and_op", and_op)
# cv2.imshow("or_op", or_op)
# cv2.imshow("xor_op", xor_op)
# cv2.imshow("not_op", not_op)
cv2.imshow("not_messi", cv2.bitwise_not(img3))

cv2.waitKey(0)
cv2.destroyAllWindows()
