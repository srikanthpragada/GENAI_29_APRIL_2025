# pip install -q streamlit
import streamlit as st
from huggingface_hub import InferenceClient
import keys

model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)


st.title("English to Hindi")
text = st.text_input("Enter English text", "How are you?" )  # textbox
if len(text) > 0:
    # convert english to hindi
    response = client.translation(text)
    st.write(response.translation_text)
     