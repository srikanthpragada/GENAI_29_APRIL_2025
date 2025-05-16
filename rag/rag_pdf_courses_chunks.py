from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import keys 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Split docs into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400, 
    chunk_overlap=100)

chunks = splitter.split_documents(docs)
print("No. of chunks :", len(chunks))

# Facebook AI Similarity Search
db = FAISS.from_documents(chunks, 
      HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

print('Created FAISS index')

question = "What is the duration of Generative AI course?"

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, provider="hf-inference", token=keys.HUGGINGFACEKEY, timeout=120)


retriever = db.as_retriever()
results = retriever.invoke(question)

context = " ".join([doc.page_content for doc in results])

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
