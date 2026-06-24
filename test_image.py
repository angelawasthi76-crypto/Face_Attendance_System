import cv2
import numpy as np

path = "dataset/ANGEL AWASTHI.jpg"

image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

print("Shape:", image.shape)
print("dtype:", image.dtype)
print("Number of channels:", image.shape[2] if len(image.shape)==3 else 1)
print("Min:", np.min(image))
print("Max:", np.max(image))