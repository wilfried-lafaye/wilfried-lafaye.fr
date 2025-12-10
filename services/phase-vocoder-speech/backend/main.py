import os
import shutil
import uuid
from typing import Optional

from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from audio_processor import AudioProcessor
from config import Config

app = FastAPI(title="Phase Vocoder Speech API")

# Mount React Frontend (after build)
# Check if dist exists to allow local dev without dist
frontend_dist = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "dist")
if os.path.exists(frontend_dist):
    # Mount assets folder
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="assets")


# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AudioProcessor
audio_processor = AudioProcessor()

# Ensure directories exist
Config.ensure_directories()

class ProcessRequest(BaseModel):
    file_id: str
    effect: str
    params: dict

@app.get("/")
async def root():
    # Serve React App
    if os.path.exists(frontend_dist):
        return FileResponse(os.path.join(frontend_dist, "index.html"))
    return {"message": "Audio Vocoder API is running (Frontend not built)"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload an audio file and return a file ID.
    """
    if not Config.is_supported_format(file.filename):
        raise HTTPException(status_code=400, detail="Unsupported file format")

    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    filename = f"{file_id}{ext}"
    
    # Save to uploaded directory
    upload_path = os.path.join(Config.TEMP_AUDIO_PATH, 'uploaded', filename)
    
    try:
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")

    return {"file_id": file_id, "filename": filename, "original_name": file.filename}


@app.post("/process-json")
async def process_audio_json(request: ProcessRequest):
    """
    Process audio using a previously uploaded file ID.
    """
    # Find the input file
    uploaded_dir = os.path.join(Config.TEMP_AUDIO_PATH, 'uploaded')
    input_filename = None
    
    # Look for file with this ID (ignoring extension knowledge if possible, or store extension map)
    # A cleaner way is to look up the file in the dir
    for f in os.listdir(uploaded_dir):
        if f.startswith(request.file_id):
            input_filename = f
            break
            
    if not input_filename:
        raise HTTPException(status_code=404, detail="File not found")

    input_path = os.path.join(uploaded_dir, input_filename)
    
    # Prepare output path
    output_filename = f"processed_{request.file_id}_{request.effect}.wav"
    output_path = os.path.join(Config.TEMP_AUDIO_PATH, 'processed', output_filename)

    try:
        # Process
        processed_audio, sample_rate = audio_processor.process_audio(
            input_path, request.effect, request.params
        )
        # Save
        audio_processor.save_audio(processed_audio, sample_rate, output_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
        # For debugging detailed errors:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "processed_file_id": f"{request.file_id}_{request.effect}",
        "url": f"/audio/processed/{output_filename}"
    }

@app.get("/audio/{kind}/{filename}")
async def get_audio(kind: str, filename: str):
    """
    Serve audio files.
    kind: 'uploaded' or 'processed'
    """
    if kind not in ['uploaded', 'processed']:
        raise HTTPException(status_code=400, detail="Invalid audio kind")
        
    base_dir = os.path.join(Config.TEMP_AUDIO_PATH, kind)
    file_path = os.path.join(base_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
        
    return FileResponse(file_path)

@app.get("/effects")
async def get_effects():
    """
    Get available effects and their default parameters.
    """
    # We need to expose effect metadata. 
    # Since existing classes only have get_parameter_widgets (Streamlit specific),
    # We should probably inspect them or just hardcode metadata for the frontend 
    # or quick-patch the effect classes to return a param schema.
    # For now, I'll return a hardcoded schema that matches the Python logic 
    # to keep it simple, or I can read it dynamically if I improve the classes.
    
    return {
        "effects": [
            {
                "id": "robot",
                "name": "Robot",
                "params": [
                    {"name": "carrier_freq", "type": "number", "default": 30.0, "min": 10, "max": 200, "label": "Carrier Frequency"}
                ]
            },
            {
                "id": "pitch",
                "name": "Pitch Shift",
                "params": [
                    {"name": "n_steps", "type": "number", "default": 4.0, "min": -12, "max": 12, "step": 1, "label": "Semitones"}
                ]
            },
            {
                "id": "speed",
                "name": "Speed Change",
                "params": [
                    {"name": "speed_factor", "type": "number", "default": 1.5, "min": 0.5, "max": 2.0, "step": 0.1, "label": "Speed Factor"}
                ]
            },
            {
                "id": "echo",
                "name": "Echo",
                "params": [
                    {"name": "delay", "type": "number", "default": 0.2, "min": 0.05, "max": 1.0, "label": "Delay (s)"},
                    {"name": "decay", "type": "number", "default": 0.5, "min": 0.1, "max": 0.9, "label": "Decay"}
                ]
            }
        ]
    }
