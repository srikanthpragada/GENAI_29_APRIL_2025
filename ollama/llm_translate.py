from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="llama3.2:latest")
prompt = """Simply translate the text from english text to Hindi:

What are you learning today?

"""
print(model.invoke(prompt)) 
