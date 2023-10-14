from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from image_speech import app
from fastapi.staticfiles import StaticFiles

# Enable CORS from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# serve the template
@app.get('/')
async def read_root():
    return FileResponse("templates/index.html")

# serve the static files
@app.get("static/{file_path}")
async def read_static_files(file_path: str):
    return FileResponse(f"static/{file_path}")

# serve the generated audio output
@app.get("/output/{audio_file}")
async def read_audio(audio_file: str):
    return FileResponse(f"output/{audio_file}")


# main only runs when called
if __name__ == "__main__":
    app = FastAPI()
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
