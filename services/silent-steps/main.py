from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import redirect_stdout
import io
import sys
import uuid
from typing import Dict

# Import the game logic
from game import Game

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for game sessions
# Key: session_id, Value: Game instance
sessions: Dict[str, Game] = {}

class CommandRequest(BaseModel):
    session_id: str
    command: str

class StartResponse(BaseModel):
    session_id: str
    output: str

class CommandResponse(BaseModel):
    output: str

def capture_output(func, *args, **kwargs):
    """Captures stdout from a function call."""
    f = io.StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

@app.post("/start", response_model=StartResponse)
def start_game():
    """Starts a new game session."""
    session_id = str(uuid.uuid4())
    game = Game()
    
    # Setup and Welcome
    # We need to manually call setup and print_welcome and capture their output
    # game.play() has a while loop, so we can't call it directly.
    
    f = io.StringIO()
    with redirect_stdout(f):
        game.setup()
        game.print_welcome()
    
    sessions[session_id] = game
    return {"session_id": session_id, "output": f.getvalue()}

@app.post("/command", response_model=CommandResponse)
def process_command(request: CommandRequest):
    """Processes a player command."""
    session_id = request.session_id
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found. Please restart the game.")
    
    game = sessions[session_id]
    
    if game.finished:
        return {"output": "The game has ended. Please refresh to start again."}

    f = io.StringIO()
    with redirect_stdout(f):
        # game.process_command returns True/False, but prints the result
        game.process_command(request.command)
    
    output = f.getvalue()
    
    # Check if game finished after command (logic in game.py might set self.finished)
    if game.finished:
        output += "\n[GAME OVER]"

    return {"output": output}

@app.get("/health")
def health_check():
    return {"status": "ok"}
