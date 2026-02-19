import cv2
import mediapipe as mp

mpose = mp.solutions.pose #inisiasi mediapipe pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) #video dari webcam

while True:
    success, img = cap.read() #pembacaan image
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgRGB) #ekstrasi dari image

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS) #menggambar koneksi landmark

        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)

    cv2.imshow('webcam', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break #tutup webcam dan jendela tampilan saat "q" ditekan

cap.release()
cv2.destroyAllWindows()
