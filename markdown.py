from IPython.display import Markdown
import os as os
from google import generativeai as genai
import PIL.Image

os.environ['GOOGLE_API_KEY']="apikey"



genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model=genai.GenerativeModel('gemini-pro')
response=model.generate_content("what are top 5 frequently used emojis?")


print(response.text)
print(response.prompt_feedback)