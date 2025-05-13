"""
!pip install -qU langchain_community
!pip install -qU langchain_huggingface
!pip install -qU langchain.text_splitter
!pip install -qU langchain.document_loaders
!pip install -qU langchain.vectorstores
!pip install -qU langchain.embeddings

"""

from huggingface_hub import InferenceClient

# Get HF Key
from google.colab import userdata
hugging_face_key = userdata.get('HUGGINGFACE_KEY')

model_id = "mistralai/Mistral-7B-Instruct-v0.3"
client = InferenceClient(model=model_id, token = hugging_face_key)

response = client.text_generation(
    "Who won FIFA world cup in 1994. Just country name please.")
print(response)

