import cv2
import numpy as np


def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    return cv2.bitwise_and(image, mask)


def draw_lines(image, hough_lines):
    copy_img = np.copy(image)
    blank_img = np.zeros((copy_img.shape[0], copy_img.shape[1], 3), np.uint8)
    for line in hough_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank_img, (x1, y1), (x2, y2), (255, 0, 0), 4)
    return cv2.addWeighted(copy_img, 0.8, blank_img, 1, 0.0)


def process(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_img, 100, 200)

    height, width = img.shape[:-1]
    roi_vertices = [(0, height), (width/2, height/2), (width, height)]

    cropped_img = roi(canny_img, np.array([roi_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_img, rho=6, theta=np.pi/60,
                            threshold=160, lines=np.array([]),
                            minLineLength=40, maxLineGap=25)
    return draw_lines(img, lines)


cap = cv2.VideoCapture('../images/traffic.mp4')
while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow("Video", process(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
