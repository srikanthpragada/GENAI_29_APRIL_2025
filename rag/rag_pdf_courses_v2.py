from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
import keys 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, 
      HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

print('Created FAISS index')

question = "Generative AI course fee"


repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, provider="hf-inference", token=keys.HUGGINGFACEKEY, timeout=120)


retriever = db.as_retriever()
results = retriever.invoke(question)

context = "\n".join([doc.page_content for doc in results])

prompt = f"""
Please answer the question using the context.

{context}

Question: {question}
Answer: 
"""


print(prompt)
print("-" * 50)

result =  llm.text_generation(prompt)
print(result)
