# Audio Vocoder Pro 🎵

A premium audio processing application featuring a modern React frontend and a powerful Python FastAPI backend. Apply advanced effects like Robot, Pitch Shift, and Echo with real-time visualization.

## 🚀 Features

-   **Modern UI**: Sleek, dark-mode interface built with React, Tailwind CSS, and Framer Motion.
-   **Real-time Visualization**: Interactive waveform visualization using Wavesurfer.js.
-   **Advanced Effects**:
    -   **🤖 Robot Effect**: Ring modulation for robotic voice.
    -   **🎼 Pitch Shift**: Change pitch without altering speed.
    -   **⏩ Speed Change**: Time stretching.
    -   **🔊 Echo**: customizable delay and decay.
-   **FastAPI Backend**: Robust audio processing using Librosa.

## 🛠️ Tech Stack

### Frontend
-   **React** (Vite)
-   **Tailwind CSS** (Styling)
-   **Framer Motion** (Animations)
-   **Wavesurfer.js** (Visualization)

### Backend
-   **FastAPI** (API Framework)
-   **Librosa** (Audio Processing)
-   **NumPy / SciPy** (Signal Processing)

## 📦 Installation & Usage

### Prerequisites
-   **Node.js** (v18+)
-   **Python** (3.10+)
-   **FFmpeg** (for audio compatibility)

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Server
uvicorn main:app --reload --port 8000
```
*The backend runs on `http://localhost:8000`*

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start Dev Server
npm run dev
```
*The frontend runs on `http://localhost:3000` (or the port shown in terminal)*

## 🎮 How to Use

1.  Open the frontend URL.
2.  **Upload** an audio file (.wav, .mp3).
3.  Use the **Controls** panel to select an effect (e.g., Robot).
4.  Adjust parameters.
5.  Click **Apply Processing**.
6.  Play the result or download it.

## 📂 Project Structure

```
phase-vocoder-speech/
├── backend/            # Python FastAPI Server
│   ├── main.py
│   ├── audio_processor.py
│   └── effects/
├── frontend/           # React Application
│   ├── src/
│   │   ├── components/
│   │   └── lib/
│   └── tailwind.config.js
└── README.md
```

## 📄 License
MIT License
