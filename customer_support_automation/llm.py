import os 

from langchain_google_genai import ChatGoogleGenerativeAI

api_key = os.getenv("GOOGLE_API_KEY")

def get_llm() -> ChatGoogleGenerativeAI:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    return llm