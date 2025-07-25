from flask import Flask, render_template, request, jsonify, send_file
import os

from dotenv import load_dotenv
load_dotenv()

import whisper
import yt_dlp
from groq import Groq
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the base Whisper model
model = whisper.load_model("base")

# Groq API client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCOPES = ['https://www.googleapis.com/auth/documents']

DOWNLOADS_DIR = "downloads"

# Ensure the downloads directory exists
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download-audio', methods=['POST'])
def download_audio():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'No URL provided'}), 400

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{DOWNLOADS_DIR}/%(id)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_id = info_dict.get("id")
            video_title = info_dict.get("title")
            thumbnail_url = info_dict.get("thumbnail")
            mp3_file = os.path.join(DOWNLOADS_DIR, f"{video_id}.mp3")

        if not os.path.exists(mp3_file):
            return jsonify({'error': 'Failed to process MP3 file'}), 500

        return send_file(mp3_file, as_attachment=True, download_name=f"{video_id}.mp3", mimetype="audio/mpeg"), 200, {
            "X-Video-Title": video_title,
            "X-Video-Thumbnail": thumbnail_url
        }

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Check if file is received
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        # Get audio file
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        # Save file to a directory
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        # Transcribe the audio (assuming model.transcribe is correctly implemented)
        result = model.transcribe(file_path)
        transcription = result['text']

        # Return transcription as JSON response
        return jsonify({'transcription': transcription})

    except Exception as e:
        # Log error message for debugging
        print("Error occurred:", e)
        return jsonify({'error': str(e)}), 500


# API route to modify text using Groq API
@app.route('/modify', methods=['POST'])
def modify_text():
    data = request.json
    user_input = data.get("modification_input")
    transcription = data.get("transcription")

    # Modify transcription using Groq API (Llama3-8b-8192 model)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{
            "role": "user",
            "content": f"Modify this content as {user_input} {transcription}"
        }],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    modified_text = ""
    for chunk in completion:
        modified_text += chunk.choices[0].delta.content or ""

    return jsonify({'modified_text': modified_text})


# Entry point for WSGI
if __name__ == "__main__":
    # Ensure uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True, host='0.0.0.0', port=5000) 