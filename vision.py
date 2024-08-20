from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
  if input != "":
    response=model.generate_content([input, image])
  else:
    response=model.generate_content(image)
  return response.text



st.set_page_config(
  page_title="Q&A Demo",
)

st.header("Gemini Application")

input = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
image=""

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Imagem carregada.', use_column_width=True)

submit = st.button("Enviar")

if submit:
  response=get_gemini_response(input, image)
  st.subheader("Resposta: ")
  st.write(response)