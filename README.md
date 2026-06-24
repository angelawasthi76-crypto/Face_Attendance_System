# 🎓 Face Recognition Attendance System

A Python-based automated attendance system that uses **face recognition** to track student attendance during lectures — recording entry time, exit time, and total class duration for each student.

---

## 📌 Features

- 🔍 **Real-time face detection and recognition** using a webcam
- 🕐 **Entry & Exit time logging** for each student per lecture
- ⏱️ **Class duration tracking** — calculates how long each student was present
- 📊 **Attendance reports** exported to Excel (`.xlsx`)
- 🗄️ **SQLite database** for persistent attendance storage
- 🧑‍🤝‍🧑 Supports **multiple students** with individual face datasets

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| OpenCV | Video capture & image processing |
| face_recognition | Face detection & recognition |
| dlib | Underlying face encoding model |
| SQLite | Attendance database storage |
| openpyxl | Excel report generation |

---

## 📁 Project Structure

```
Face_Attendance_System/
│
├── attendance_system.py      # Main application — runs the attendance system
├── train_faces.py            # Train face encodings from dataset images
├── database_manager.py       # Handles all database operations
├── export_excel.py           # Exports attendance records to Excel
├── utils.py                  # Utility/helper functions
├── test_dlib.py              # Test dlib installation
├── test_image.py             # Test face recognition on a single image
│
├── dataset/                  # Student face images (one image per student)
│   ├── STUDENT NAME.jpg
│   └── ...
│
├── database/
│   └── attendance.db         # SQLite attendance database
│
├── models/                   # Saved face encodings (generated after training)
│
├── reports/                  # Auto-generated Excel attendance reports
│
└── requirements.txt          # Python dependencies
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/angelawasthi76-crypto/Face_Attendance_System.git
cd Face_Attendance_System
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note:** `dlib` can be tricky to install. If you face issues, install the pre-built wheel directly:
> ```bash
> pip install dlib-19.24.6-cp311-cp311-win_amd64.whl
> ```

---

## 🚀 Usage

### Step 1: Add student images
Place one clear face photo per student inside the `dataset/` folder.  
Name the file exactly as the student's name (e.g., `ANGEL AWASTHI.jpg`).

### Step 2: Train the model
```bash
python train_faces.py
```
This generates face encodings and saves them in the `models/` folder.

### Step 3: Run the attendance system
```bash
python attendance_system.py
```
The webcam will open and start recognizing students in real time.  
Entry and exit times are automatically logged to the database.

### Step 4: Export attendance report
```bash
python export_excel.py
```
An Excel report is saved in the `reports/` folder with student names, entry time, exit time, and duration.

---

## 📊 Sample Attendance Report

| Student Name | Entry Time | Exit Time | Duration |
|--------------|------------|-----------|----------|
| Angel Awasthi | 10:00:05 AM | 11:45:32 AM | 1h 45m |
| Anant Pathak | 10:01:12 AM | 11:44:58 AM | 1h 43m |

---

## 🔧 Requirements

- Python 3.11
- Webcam / USB camera
- Windows 10/11 (tested)
- CMake (required for dlib compilation)

---

## 👩‍💻 Author

**Angel Awasthi**  
B.Tech Computer Science — Medicaps University, Indore (2027)  
Google AI/ML Developer Program Participant  

---

## 📄 License

This project is for educational purposes as part of academic coursework.
