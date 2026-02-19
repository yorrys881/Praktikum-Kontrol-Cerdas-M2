import cv2
import mediapipe as mp
mpose = mp.solutions.pose #inisialisasi mediapipe pose
pose = mpose.Pose(static_image_mode=False, model_complexity=1, smooth_landmarks=True, enable_segmentation=False, smooth_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0) #video dari webcam 1

while True:
    success, img = cap.read() #pembacaan image
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstrasi dari image

    if hasil.pose_landmarks :
        print("terdeteksi")
    else:
        print("tidak terdeteksi")

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() #tutup webcam dan jendela tampilan saat "q" ditekan
cv2.destroyAllWindows()