import os
from dotenv import load_dotenv

load_dotenv()

def get_provider_name() -> str:
    return "GROQ"

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set in environment. Please check your .env file.")
    
    model = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    
    try:
        from langchain_groq import ChatGroq
        return ChatGroq(
            api_key=api_key, 
            model=model, 
            temperature=0.2, 
            streaming=True
        )
    except ImportError:
        raise ImportError("langchain_groq is not installed. Please run 'pip install langchain-groq'")