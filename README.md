# Hindi2English-NLLB-Translate
Hindi to English NLLB-200 translator API. This is an API used for translating sentences from Hindi to English accurately. It uses Python as the programming language and FastAPI as the web framework. It makes use of a pre-trained model created by facebook named "facebook/nllb-200-distilled-600M".  

# Getting Started  
To install, run the [requirements.txt](requirements.txt) using the following command:  

```
pip install -r requirements.txt
```

# Hugging Face Key  
Place your Hugging Face API key in the ```main.py``` file in place of ```your_actual_hugging_face_api_key``` or you can place it in a ```.env``` file and access it in your code.  

# Run the Application
Run the main.py file by following command:
```
uvicorn main:app --reload
```
Then, open your localhost http://127.0.0.1:8000 to see it on your browser.  

# Home Page  
The below image illustrates the implementation of this translator with a simple UI.  
You can enter the input Hindi text in the text box given there and click on ```Translate``` button which directs to result page.  
  
![image](https://github.com/user-attachments/assets/b167e309-5d68-4bbd-be4e-ab78b2917f2d)  

# Result page  
In this page, you can see the input Hindi text, The translated English text and an option to translate other texts as follows:  
  
![image](https://github.com/user-attachments/assets/214f5a40-b3c0-4293-892d-18fc9ab4957d)  

# Learn More  
To learn more about FastAPI and NLLB-200, look at the following resources:  
[NLLB-200 Model](https://huggingface.co/facebook/nllb-200-distilled-600M) - Explore NLLB-200 here.  
[FastAPI Documentation](https://fastapi.tiangolo.com/) - Learn FastAPI in detail from this documentation.  
