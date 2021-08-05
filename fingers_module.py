import numpy as np
import cv2
import hand_tracking_module as hand_module
import time


class Fingers(hand_module.HandDetector):
    def __init__(self, mode=False, max_num_hands=2, detection_confidence=0.5, track_confidence=0.5):
        super(Fingers, self).__init__(mode, max_num_hands, detection_confidence, track_confidence)
        self.thumb_mcp_id = 2
        self.thumb_tip_id = 4
        self.index_pip_id = 6
        self.index_tip_id = 8
        self.middle_pip_id = 10
        self.middle_tip_id = 12
        self.ring_pip_id = 14
        self.ring_tip_id = 16
        self.pinky_pip_id = 18
        self.pinky_tip_id = 20
        self.tip_ids = np.array([4, 8, 12, 16, 20])
        self.pip_ids = self.tip_ids - 2
        self.up_fingers = []
        self.index = None
        self.middle = None

    def identify_up_fingers(self):
        self.up_fingers = []
        # thumb finger case is different check x value instead
        # check whether it's left or right hand
        # left hand the wrist x value is higher than the thumb pip
        if self.landmarks[0][1] > self.landmarks[self.pip_ids[0]][1]:  # left hand
            if self.landmarks[self.tip_ids[0]][1] < self.landmarks[self.tip_ids[0] - 1][1]:
                self.up_fingers.append(1)
            else:
                self.up_fingers.append(0)
        elif self.landmarks[0][1] < self.landmarks[self.pip_ids[0]][1]:  # right hand
            if self.landmarks[self.tip_ids[0]][1] > self.landmarks[self.tip_ids[0] - 1][1]:
                self.up_fingers.append(1)
            else:
                self.up_fingers.append(0)

        for idx in range(1, self.tip_ids.shape[0]):
            if self.landmarks[self.tip_ids[idx]][2] < self.landmarks[self.pip_ids[idx]][2]:
                self.up_fingers.append(1)
            else:
                self.up_fingers.append(0)
        if self.up_fingers[1]:
            self.index = True
        else:
            self.index = False
        if self.up_fingers[2]:
            self.middle = True
        else:
            self.middle = False
        return self.up_fingers


def main():
    prev_time = 0
    cap = cv2.VideoCapture(0)
    fingers = Fingers()
    while cap.isOpened():
        success, img = cap.read()
        img = fingers.find_hands(img)
        lm_list = fingers.find_position(img)
        if len(lm_list) != 0:
            up_fingers = fingers.identify_up_fingers()
            print(fingers.middle)
            print(up_fingers)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()