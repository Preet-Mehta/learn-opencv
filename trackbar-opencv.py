import cv2
import numpy as np


def change_color(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, change_color)
cv2.createTrackbar('G', 'image', 0, 255, change_color)
cv2.createTrackbar('R', 'image', 0, 255, change_color)
cv2.createTrackbar('O:OFF, 1:ON', 'image', 0, 1, change_color)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF

    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos('O:OFF, 1:ON', 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    if key == 27:
        break

cv2.destroyAllWindows()
