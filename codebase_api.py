import os
from fastapi import FastAPI
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI(title="Codebase Q&A API",
              version="1.0",
              description="An AI-powered REST API to analyze and answer questions about your codebase.")

# Step 1: Load the codebase from your project directory
project_directory = "C:/Users/YourUsername/HackathonProject"  # Change to your actual path
loader = DirectoryLoader(project_directory, glob="**/*.py")
documents = loader.load()

# Step 2: Split the code into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
code_chunks = text_splitter.split_documents(documents)

# Step 3: Convert code into AI-searchable vector embeddings
vector_db = FAISS.from_documents(code_chunks, OpenAIEmbeddings())
retriever = vector_db.as_retriever()

# Step 4: Load AI Model (Groq Llama3-8b-8192)
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Step 5: Create a Q&A System for the Codebase
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

# API Route: Ask a question about the codebase
@app.get("/ask/")
async def ask_codebase(query: str):
    """Ask a question about the codebase and get an AI-generated answer"""
    response = qa_chain.run(query)
    return {"question": query, "answer": response}

# Run the API using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
