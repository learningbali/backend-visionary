from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Mengizinkan GitHub Pages mengakses Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Menggunakan "*" agar tidak diblokir Vercel saat testing
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
    # Parameter dasar
    base = "Ultra-Realistic Cinematic ASMR Commercial. Photorealistic, 8K quality, Editorial product photography. "
    neg = "No music. No dialogue. No face visible."
    
    # Hasil simulasi
    return [
        StoryboardSegment(
            timecode="0:00 - 0:02", 
            prompt=f"{base} Macro close-up of a precision screwdriver tightening a screw into a diecast sports car. {neg}"
        ),
        StoryboardSegment(
            timecode="0:03 - 0:04", 
            prompt=f"{base} Extreme close-up of vintage metal model train wheels locking onto tracks. {neg}"
        )
    ]
