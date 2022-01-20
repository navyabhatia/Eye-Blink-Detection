import cv2
import numpy as np
import dlib
import math
BLINK_RATIO_THRESHOLD=5.7
def midpoint(point1 ,point2):
    return int((point1.x + point2.x)/2), int((point1.y + point2.y)/2)
def euclidean_distance(point1 , point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
def get_blink_ratio(eye_points, facial_landmarks):
    # loading all the required points
    corner_left = (facial_landmarks.part(eye_points[0]).x,
                   facial_landmarks.part(eye_points[0]).y)
    corner_right = (facial_landmarks.part(eye_points[3]).x,
                    facial_landmarks.part(eye_points[3]).y)

    center_top = midpoint(facial_landmarks.part(eye_points[1]),
                          facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]),
                             facial_landmarks.part(eye_points[4]))

    # calculating distances
    horizontal_length = euclidean_distance(corner_left, corner_right)
    vertical_length = euclidean_distance(center_top, center_bottom)

    ratio = horizontal_length / vertical_length

    return ratio

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
left_eye_landmarks = [36, 37, 38, 39, 40, 41]
right_eye_landmarks = [42, 43, 44, 45, 46, 47]

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        landmarks = predictor(gray, face)
        left_point = (landmarks.part(36).x, landmarks.part(36).y)
        right_point = (landmarks.part(39).x, landmarks.part(39).y)
        centre_top = midpoint(landmarks.part(37), landmarks.part(38))
        centre_bottom = midpoint(landmarks.part(41), landmarks.part(40))
        left_point1 = (landmarks.part(42).x, landmarks.part(42).y)
        right_point1 = (landmarks.part(45).x, landmarks.part(45).y)
        centre_top1 = midpoint(landmarks.part(43), landmarks.part(44))
        centre_bottom1 = midpoint(landmarks.part(47), landmarks.part(46))
        hor_line = cv2.line(frame, left_point, right_point, (0, 255, 255), 2)
        ver_line = cv2.line(frame, centre_top, centre_bottom, (255, 255, 0), 2)
        hor_line1 = cv2.line(frame, left_point1, right_point1, (0, 255, 255), 2)
        ver_line1 = cv2.line(frame, centre_top1, centre_bottom1, (255, 255, 0), 2)

        for n in range(36, 48):    #initially (0,68) for full coordinates
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

        left_eye_ratio = get_blink_ratio(left_eye_landmarks, landmarks)
        right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
        blink_ratio = (left_eye_ratio + right_eye_ratio) / 2
        if blink_ratio > BLINK_RATIO_THRESHOLD:
            # Blink detected! Do Something!
            cv2.putText(frame, "BLINKING", (10, 50), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
