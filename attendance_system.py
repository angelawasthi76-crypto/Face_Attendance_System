import cv2
import face_recognition
import pickle
from datetime import datetime

from database_manager import *
from utils import *

with open("models/face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

present_students = {}

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb)

    encodings = face_recognition.face_encodings(rgb, locations)

    for encoding, location in zip(encodings, locations):

        matches = face_recognition.compare_faces(
            known_encodings,
            encoding
        )

        name = "Unknown"

        distances = face_recognition.face_distance(
            known_encodings,
            encoding
        )

        if len(distances) > 0:

            best_match = distances.argmin()

            if matches[best_match]:
                name = known_names[best_match]

        top, right, bottom, left = location

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        if name != "Unknown":

            date = current_date()

            if name not in present_students:

                entry_time = current_time()

                present_students[name] = entry_time

                mark_entry(
                    name,
                    date,
                    entry_time
                )

                print(name, "entered at", entry_time)

    cv2.imshow("Attendance System", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

from database_manager import cursor

date = current_date()

for student in present_students:

    exit_time = current_time()

    mark_exit(
        student,
        date,
        exit_time
    )

    cursor.execute("""
    SELECT entry_time
    FROM attendance
    WHERE name=? AND date=?
    """, (student, date))

    entry_time = cursor.fetchone()[0]

    duration = calculate_duration(
        entry_time,
        exit_time
    )

    update_duration(
        student,
        date,
        duration
    )
cap.release()
cv2.destroyAllWindows()