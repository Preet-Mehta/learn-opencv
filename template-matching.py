import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.imread('images/messi_face.jpg', 0)
h, w = face.shape[::]

res = cv2.matchTemplate(gray, face, cv2.TM_CCOEFF_NORMED)
threshold_value = 0.95
match = np.where(res >= threshold_value)

for i in zip(*match[::-1]):
    cv2.rectangle(img, i, (i[0]+w, i[1]+h), (0, 255, 0), 2)

# cv2.imshow('Res', res)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
