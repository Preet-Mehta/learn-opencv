import cv2

cap = cv2.VideoCapture('images/vtest.avi')

_, frame1 = cap.read()

while cap.isOpened():
    _, frame2 = cap.read()
    diff = cv2.absdiff(frame2, frame1)
    # cv2.imshow('Diff', diff)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Gray', gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow('Blur', blur)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # cv2.imshow('Thresh', thresh)
    dilated = cv2.dilate(thresh, None, iterations=3)
    # cv2.imshow('Dilated', dilated)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    # cv2.imshow('Contours', frame1)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 900:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, f"Status: Movement", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    cv2.imshow('Final', frame1)
    frame1 = frame2

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()
