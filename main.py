from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI()

# MENGIZINKAN GITHUB PAGES ANDA UNTUK MENGAKSES BACKEND INI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://learningbali.github.io"], # URL GitHub Anda
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StoryboardSegment(BaseModel):
    timecode: str
    prompt: str

@app.post("/api/process-video", response_model=list[StoryboardSegment])
async def process_video(
    youtube_url: str = Form(None),
    style_preference: str = Form("dokumenter")
):
    time.sleep(2) # Simulasi loading
    
    # Base prompt
    base = "Ultra-Realistic Cinematic ASMR Commercial. Photorealistic, 8K quality, Editorial product photography. "
    neg = "No music. No dialogue. No face visible."
    
    # Simulasi hasil
    return [
        StoryboardSegment(timecode="0:00 - 0:02", prompt=f"{base} Macro close-up of a precision screwdriver tightening a screw into a diecast sports car. {neg}"),
        StoryboardSegment(timecode="0:03 - 0:04", prompt=f"{base} Extreme close-up of vintage metal model train wheels locking onto tracks. {neg}")
    ]
