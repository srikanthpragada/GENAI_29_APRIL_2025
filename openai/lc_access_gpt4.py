from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import keys 
import os 

os.environ["OPENAI_API_KEY"] = keys.OPENAIKEY

# Create an OpenAI LLM instance
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Run a query
response = llm.invoke([HumanMessage(content="What is the capital of France?")])
print(response.content)

