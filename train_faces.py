import face_recognition
import cv2
import os
import pickle

known_encodings = []
known_names = []

dataset_path = "dataset"

for file in os.listdir(dataset_path):

    try:
        path = os.path.join(dataset_path, file)

        print("Processing:", file)

        image = cv2.imread(path, cv2.IMREAD_COLOR)

        if image is None:
            print("Cannot read:", file)
            continue

        # Force conversion to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert to uint8 if necessary
        image = image.astype("uint8")

        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print("No face found:", file)
            continue

        known_encodings.append(encodings[0])

        name = os.path.splitext(file)[0]
        known_names.append(name)

    except Exception as e:
        print("Error in", file)
        print(e)

print("Total students =", len(known_names))

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open("models/face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Training completed")