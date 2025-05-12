from huggingface_hub import InferenceClient
import keys 
model_id = "meta-llama/Llama-3.1-8B-Instruct"
client = InferenceClient(model=model_id, provider = "hf-inference",
                         token=keys.HUGGINGFACE_KEY)

response = client.text_generation("What is the capital of France?")
print(response)
