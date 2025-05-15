from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
client = InferenceClient(model=model_id, provider="hf-inference", token=keys.HUGGINGFACE_KEY)

response = client.text_generation("What is the capital of France?")
print(response)
