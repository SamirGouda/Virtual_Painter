import cv2
import numpy as np
import time
import os
import fingers_module as fm

# import header images
image_list = os.listdir('headers')
headers = []
for img in image_list:
    img_path = os.path.join('headers', img)
    image = cv2.imread(img_path)
    headers.append(image)
header = headers[0]
canvas_image = np.zeros((480, 640, 3), dtype=np.uint8)
color = (255, 0, 255)
brush_thickness = 10
xp, yp = 0, 0

prev_time = 0
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

fingers = fm.Fingers(max_num_hands=1, detection_confidence=0.8)

while cap.isOpened():
    # take a snapshot from webcam
    success, img = cap.read()
    # flip image to reverse webcam effect
    img = cv2.flip(img, 1)
    # identify hand landmarks
    img = fingers.find_hands(img)
    landmarks = fingers.find_position(img, False)

    if len(landmarks) != 0:
        # identify fingers
        up_fingers = fingers.identify_up_fingers()
        index = landmarks[fingers.index_tip_id][1:]
        x1, y1 = index
        middle = landmarks[fingers.middle_tip_id][1:]
        brush_thickness = np.linalg.norm(np.array(index)-np.array(middle), 2)
        brush_thickness = int(np.interp(brush_thickness, (15, 75), (10, 50)))
        # select mode
        if fingers.index and fingers.middle:
            # reset initial coordinates
            xp, yp = 0, 0
            print('selection mode')
            # select item
            if index[1] < 125:
                if 0 < index[0] < 155:
                    header = headers[0]
                    color = (255, 0, 255)
                if 185 < index[0] < 305:
                    header = headers[1]
                    color = (255, 0, 0)
                if 335 < index[0] < 455:
                    header = headers[2]
                    color = (0, 255, 0)
                if 485 < index[0] < 640:
                    header = headers[3]
                    color = (0, 0, 0)
            cv2.rectangle(img, index, middle, color, cv2.FILLED)
        elif fingers.index and not fingers.middle:
            cv2.circle(img, index, 15, color, cv2.FILLED)
            print('draw mode')
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.line(img, (xp, yp), (x1, y1), color, brush_thickness)
            cv2.line(canvas_image, (xp, yp), (x1, y1), color, brush_thickness)
            xp, yp = x1, y1

    img_gray = cv2.cvtColor(canvas_image, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas_image)
    # setting the header
    img[:125, :] = header
    # img = cv2.addWeighted(img, 0.5, canvas_image, 0.5, 0)
    cv2.imshow('virtual painter', img)
    cv2.imshow('virtual painter1', canvas_image)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break