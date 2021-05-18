import cv2
import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        display_text = f"Width:{cap.get(3)}, Height:{cap.get(4)}"
        display_font = cv2.FONT_HERSHEY_SIMPLEX
        cur_dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, cur_dt, (10, 50), display_font, 1, (0, 255, 255), 1)
        cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
