from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transformers import pipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY', 'your_actual_hugging_face_api_key')

from huggingface_hub import HfFolder
HfFolder.save_token(HUGGINGFACE_API_KEY)

app = FastAPI()

# Define source and target languages
source_lang = "hin_Deva"
target_lang = "eng_Latn"

# Initialize the translation pipeline
translator = pipeline(
    "translation", 
    model="facebook/nllb-200-distilled-600M", 
    tokenizer="facebook/nllb-200-distilled-600M", 
    src_lang=source_lang, 
    tgt_lang=target_lang, 
    max_length=400
)

def hindi_to_english(hindi_text: str):
    translation = translator(hindi_text)[0]['translation_text']
    return {
        "hindi_text": hindi_text,
        "english_text": translation
    }

@app.get("/", response_class=HTMLResponse)
async def form():
    html_content = """
    <html>
        <head>
            <title>Hindi to English Translator</title>
        </head>
        <body>
            <h1>Translate Hindi to English</h1>
            <form action="/translate/" method="post">
                <label for="input_hindi_text">Enter Hindi Text:</label><br><br>
                <input type="text" id="input_hindi_text" name="input_hindi_text"><br><br>
                <input type="submit" value="Translate">
            </form>
        </body>
    </html>
    """
    return html_content

@app.post("/translate/", response_class=HTMLResponse)
async def translate_hindi2english(input_hindi_text: str = Form(...)):
    translation_result = hindi_to_english(input_hindi_text)
    html_content = f"""
    <html>
        <head>
            <title>Translation Result</title>
        </head>
        <body>
            <h1>Translation Result</h1>
            <p><strong>Hindi Text:</strong> {translation_result['hindi_text']}</p>
            <p><strong>English Translation:</strong> {translation_result['english_text']}</p>
            <a href="/">Translate Another Text</a>
        </body>
    </html>
    """
    return html_content
