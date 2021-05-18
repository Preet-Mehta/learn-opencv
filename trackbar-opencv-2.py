import cv2


def change_color(x):
    print(x)


cv2.namedWindow('image')
cv2.createTrackbar('Position', 'image', 10, 400, change_color)
cv2.createTrackbar("C/G", 'image', 0, 1, change_color)

while True:
    img = cv2.imread('images/lena.jpg')
    pos = cv2.getTrackbarPos('Position', 'image')
    img = cv2.putText(img, f"{pos}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    if cv2.getTrackbarPos("C/G", 'image'):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('image', img)

cv2.destroyAllWindows()
