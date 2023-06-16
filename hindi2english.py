from fastapi import FastAPI, Query
from typing import Annotated
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from huggingface_hub import HfFolder; HfFolder.save_token("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")


app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained(
    "facebook/nllb-200-distilled-600M", use_auth_token=True, src_lang="hin_Deva"
)
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=True)

def hindi_to_english(hindi_text: str):
    inputs = tokenizer(hindi_text, return_tensors="pt")
    translated_tokens = model.generate(
    **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=30
    )
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return{
        "hindi text" : hindi_text,
        "english text": translated_text
   }


@app.get("/")
def index():
    return {"Home page": "Welcome"}

@app.post("/translate/")
async def translate_hindi2english(
    input_hindi_text: Annotated[str | None, Query(description = "Enter the hindi string to translate")] = None,
    to_translate: Annotated[bool | None, Query(description = "Enter true or false for translating")] = None,
):
    if to_translate:
        hindi_to_english(input_hindi_text)
    print(hindi_to_english(input_hindi_text))
    return{"success": True}