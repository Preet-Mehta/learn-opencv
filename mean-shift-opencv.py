import numpy as np
import cv2 as cv

cap = cv.VideoCapture('images/traffic.mp4')

# Take first frame of the video
ret, frame = cap.read()
frame = cv.resize(frame, (500, 500))

# Setup initial location of car window
x, y, width, height = 280, 270, 80, 50
track_window = (x, y, width, height)

# Setup the ROI for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
cv.imshow("ROI", roi)
term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while cap.isOpened():
    _, frame = cap.read()

    frame = cv.resize(frame, (500, 500))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply Mean Shift to get the new location
    # ret, track_window = cv.meanShift(dst, track_window, term_criteria)
    ret, track_window = cv.CamShift(dst, track_window, term_criteria)
    # Draw it on window
    # x, y, w, h = track_window
    # final_image = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)
    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 2)
    cv.imshow("dst", dst)
    cv.imshow("Final Image", final_image)
    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
