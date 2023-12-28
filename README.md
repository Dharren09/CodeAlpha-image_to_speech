# Image to Speech Converter

This is a FastAPI-based web application that allows users to convert text from an image into spoken words. It utilizes Optical Character Recognition (OCR) and text-to-speech synthesis to provide this functionality. The application provides a user-friendly web interface to upload an image, select the desired language for the audio output, and convert the text to speech.

## Features

- Convert text from images to speech in multiple languages (English, French, German).
- User-friendly web interface.
- Image preview and audio playback.
- Efficient processing with asynchronous operations.

## Prerequisites

Before running this application, make sure you have the following dependencies installed:

- Python 3.7+
- FastAPI
- Tesseract-OCR
- Pillow (PIL)
- gTTS (Google Text-to-Speech)
- Other dependencies (specified in requirements.txt)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Dharren09/CodeAlpha-image_to_speech.git

2. Navigate the project directory

   ```bash
   cd CodeAlpha-image_to_speech

3. install the required dependencies
   
   ```bash
   pip install -r requirements.txt

## Usage

1. Start the FastAPI server:
   
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload

2. Access the application in your web browser:
   
   * URL: http://localhost:8000/

3. Use the web interface to upload an image, select a language, and convert the  text to speech.

## Configuration

You can configure the application by modifying the `config.py` file. You can change the upload directory, supported languages, and other settings as needed.

## Folder Tree

   - `main.py`: The entry point for the FastAPI application.
   - `image_speech.py`: The logic for image processing and speech synthesis.
   - `templates/`: Contains HTML templates.
   - `static/`: Contains CSS and JavaScript files.
   - `output/`: Audio files are saved here.

## Contributor
   
Makoha Dharren Pius
   - `Twitter`: https://www.twitter.com/iamdevdharrenzug
   - `LinkedIn`: www.linkedin.com/in/iamdevdharrenzug
   - `Instagram`: www.instagram.com/iamdharrenz_ug

## Acknowledgments

   - `FastAPI`: https://fastapi.tiangolo.com/
   - `gTTS`: https://gtts.readthedocs.io/
   - `Tesseract-OCR`: https://github.com/tesseract-ocr/tesseract
   - `Pillow (PIL)`: https://pillow.readthedocs.io/
