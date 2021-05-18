import cv2
import numpy as np

img = cv2.imread('images/chessboard.png')
gray_img = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

dst = cv2.cornerHarris(gray_img, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.01*dst.max()] = [255, 0, 0]

cv2.imshow('dw', dst)
cv2.imshow('Final', img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
