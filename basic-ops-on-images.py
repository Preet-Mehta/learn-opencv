import cv2

img = cv2.imread('images/messi5.jpg')
img2 = cv2.imread('images/opencv-logo-white.png')

# print(img.shape)  # rows, columns, channels
# print(img.size)  # total pixels
# print(img.dtype)  # image datatype

b, g, r = cv2.split(img)  # get individual channels
img = cv2.merge((b, g, r))
# img = cv2.merge((g, r, b))

ball = img[280:340, 330:390]
img[280:340, 4:64] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
combined_img = cv2.add(img2, img)
# combined_img = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow('messi', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
