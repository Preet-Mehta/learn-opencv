import cv2
import numpy as np


# simple mouse events
def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        display_txt = f"({x},{y})"
        cv2.putText(img, display_txt, (x, y), font, 0.5, (255, 255, 0), 1)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        display_txt = f"({blue},{green},{red})"
        cv2.putText(img, display_txt, (x, y), font, 0.5, (0, 255, 255), 1)
    cv2.imshow("image", img)


# advanced mouse events
def advanced_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(img, points[-2], points[-1], (0, 0, 255), 1)
        cv2.imshow("image", img)


def more_advanced_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        new_color_img = np.zeros([512, 512, 3], np.uint8)
        cv2.imshow("new_image", new_color_img)
        new_color_img[:] = [blue, green, red]


# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('images/messi5.jpg', 1)
cv2.imshow('image', img)
points = []

cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
