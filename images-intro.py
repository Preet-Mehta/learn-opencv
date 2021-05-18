import cv2

img = cv2.imread('images/lena.jpg', -1)
cv2.imshow('Image', img)
key = cv2.waitKey(0) & 0xFF     # This masking is usually recommended for 64-bit OS.

if key == ord('s'):
    cv2.imwrite("lena_copy.png", img)

cv2.destroyAllWindows()
