import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(1)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'AVC1')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (320, 180))


while(True):
    ret, frame = cap.read()
    print frame.shape
    frame = imutils.resize(frame, width=320,height=180)
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()