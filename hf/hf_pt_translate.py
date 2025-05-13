from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
import keys

model_id = "mistralai/Mistral-7B-Instruct-v0.3"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY, provider="hf-inference")


template_en_to_hi = """Translate the following English text to simple Hindi:

{text}

"""
prompt_en_to_hi = PromptTemplate.from_template(template=template_en_to_hi)


english_text = "What did you learn about AI?"

prompt_en_to_hi = prompt_en_to_hi.format(text=english_text)
print(prompt_en_to_hi)



response = client.text_generation(prompt_en_to_hi)

# 5. Print the translation
print(f"English: {english_text}")
print(f"Hindi: {response}")
