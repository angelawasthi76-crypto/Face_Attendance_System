import cv2
import dlib

image = cv2.imread("dataset/ANGEL AWASTHI.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detector = dlib.get_frontal_face_detector()

faces = detector(image)

print("Faces detected:", len(faces))