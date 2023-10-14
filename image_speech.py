from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from PIL import Image
import pytesseract
from gtts import gTTS
import io
import os


app = FastAPI()


# directory where the audio output will be stored
output_dir = "output"

# if it doesnt exist
os.makedirs(output_dir, exist_ok=True)

class ImageText(BaseModel):
    text: str


@app.post("/image-to-speech")
async def image_to_speech(image: UploadFile, language: str = Form(...)):
    # extract text from the image using OCR
    image_data = await image.read()
    extracted_text = pytesseract.image_to_string(Image.open(io.BytesIO(image_data)))

    # logic to assemble speech according to desired lang
    lang_code = language # remember the Dafault lang=en

    if language == "fr":
        lang_code = "fr"
    elif language == "de":
        lang_code == "de"

    # convert the text to speech
    generated_speech = gTTS(extracted_text, lang=lang_code)
    audio_path = os.path.join(output_dir, f"{lang_code}.mp3")
    generated_speech.save(audio_path)

    return {"audio_path": audio_path, "language": lang_code}