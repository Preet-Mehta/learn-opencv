import cv2

cap = cv2.VideoCapture('images/vtest.avi')
# fg_bg = cv2.createBackgroundSubtractorMOG2()
fg_bg = cv2.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():
    _, frame = cap.read()
    fg_mask = fg_bg.apply(frame)

    cv2.imshow('FG Mask', fg_mask)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
