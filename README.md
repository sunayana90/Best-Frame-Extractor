🎥 Best Frame Extractor from Video

A FastAPI-based computer vision application that automatically extracts the best quality image from a video by analyzing facial attributes such as mouth state, eye openness, motion stability, sharpness, and face position.

The system intelligently selects frames during pause moments (when the face is stable), ensuring natural and professional-looking results.

🚀 Features

📤 Upload any video through a clean web UI

🎯 Adaptive frame extraction (captures more frames during pauses)

😀 Face detection using MediaPipe

👄 Mouth closed detection (rejects talking frames)

👁️ Eye-open detection (rejects blink frames)

🔍 Blur detection (prefers sharp images)

🎯 Face-centered scoring

🖼️ Automatically saves and displays the best frame

🌐 Simple, professional frontend using HTML + CSS

🧠 How It Works (High-Level)

Video Upload
User uploads a video via the browser UI.

Adaptive Frame Extraction

Normal motion → sample fewer frames

Low motion (pause) → capture more frames

Face & Landmark Analysis
Each frame is analyzed using MediaPipe:

Face detection

Facial landmarks

Quality Filters

Mouth must be closed

Eyes must be open

Image must be sharp

Face should be centered

Scoring System
Frames are scored based on:

Sharpness

Facial stability

Mouth state

Eye openness

Face position

Best Frame Selection
The frame with the highest score is saved and displayed as output.

🛠️ Tech Stack

Backend: FastAPI

Computer Vision: OpenCV, MediaPipe

Frontend: HTML, CSS, JavaScript

Server: Uvicorn

Language: Python 3.9+

📁 Project Structure
best-frame-extractor/
│
├── app/
│   ├── main.py              # FastAPI routes & server
│   ├── video_utils.py       # Adaptive frame extraction logic
│   └── frame_selector.py    # Face analysis & scoring logic
│
├── templates/
│   └── index.html           # Frontend UI
│
├── static/
│   └── style.css            # UI styling
│
├── uploads/                 # Uploaded videos
├── outputs/                 # Extracted best frame
│
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd best-frame-extractor

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
uvicorn app.main:app --reload


Open in browser:

http://127.0.0.1:8000

🧪 How to Use

Open the web app

Upload a video (talking or recorded selfie video)

Click Extract Best Frame

The system automatically selects and displays the best image

📸 Example Use Cases

Interview profile photo extraction

YouTube / content creator thumbnails

Online meeting profile pictures

Resume / portfolio photos

Automated photo capture systems

📈 Improvements Implemented

Adaptive frame sampling based on motion detection

Scale-invariant mouth closed detection

Eye blink rejection using facial landmarks

Interpretable scoring logic

Clean separation of backend and UI

🔮 Future Enhancements

Top-K best frame selection

Consecutive-frame stability (temporal smoothing)

Smile / neutral expression classification

Progress bar during processing

Download button for extracted image

Cloud deployment (Render / AWS)

🧠 Learning Outcomes

Practical use of MediaPipe Face Mesh

Real-world video frame analysis

Facial landmark–based quality checks

Designing interpretable scoring systems

Building a full ML-powered web application