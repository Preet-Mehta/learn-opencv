import numpy as np
import cv2

# img = cv2.imread('images/lena.jpg', 1)

# shape in np: imagine 1->height, 2->rows, 3->columns
img = np.zeros([510, 510, 3], np.uint8)

# # Use -1 as thickness to fill the colour in the shape.
img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 2)
img = cv2.arrowedLine(img, (255, 0), (255, 255), (255, 0, 0), 2)
img = cv2.rectangle(img, (0, 255), (255, 510), (0, 0, 255), 2)
img = cv2.circle(img, (255, 255), 255, (255, 255, 0), 2)
img = cv2.putText(img, "Hello World", (100, 360), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.imwrite("lena_drawings.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
