from PIL import Image
import google.generativeai as genai
import google.ai.generativelanguage as glm
import cv2
import numpy as np
import io

genai.configure(api_key="AIzaSyDCC37zDwAjEQW3qALuQzG9YvdVnsvPXnY")
model = genai.GenerativeModel('gemini-pro-vision')


task="Build a wall"
image_path = 'D:\Python\Onsite Gemini\images.jpg'
image = Image.open(image_path)
image = image.convert('RGB')
img_byte_arr = io.BytesIO()
image.save(img_byte_arr, format='JPEG')
prompt = f"You are an expert at reviewing employees work at a big company, you will be having a task to validate employees work by analyzing a picture, Your answer will only be Yes or NO then explain why considering the task very well\
    The task is : {task}"
blob = glm.Blob(
                mime_type='image/jpeg',
                data=img_byte_arr.getvalue()
            )
response = model.generate_content([prompt,blob],stream=True)
print(response)