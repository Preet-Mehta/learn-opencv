import cv2

img = cv2.imread('images/opencv-logo-white.png')
bin_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (255, 0, 255), 2)

cv2.imshow('Binary', bin_img)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
