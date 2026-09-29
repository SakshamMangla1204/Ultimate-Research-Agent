import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI 
from langchain_groq import ChatGroq

from config import (
    GEMINI_MODEL,
    GROQ_MODEL,
    MISTRAL_MODEL,
    MODEL_TEMPERATURE,
    DEFAULT_MODEL,

)

load_dotenv()

gemini_api_key=os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY IS NOT SET ")

gemini_llm=ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    temperature=MODEL_TEMPERATURE,
    api_key=gemini_api_key,
    
)

mistral_api_key=os.getenv("MISTRAL_API_KEY")

if not mistral_api_key:
    raise ValueError("MISTRAL_API KEY NOT FOUND")

mistral_llm=ChatMistralAI(
    model=MISTRAL_MODEL,
    temperature=MODEL_TEMPERATURE,
    api_key=mistral_api_key,

)

groq_api_key=os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY IS NOT FOUND ")

groq_llm=ChatGroq(
    model=GROQ_MODEL,
    temperature=MODEL_TEMPERATURE,
    api_key=groq_api_key,
)

if DEFAULT_MODEL=="gemini":
    llm=gemini_llm
elif DEFAULT_MODEL=="mistral":
    llm=mistral_llm
elif DEFAULT_MODEL=="groq":
    llm=groq_llm
else:
    raise ValueError(
        f"Unknown DEFAULT_MODEL:{DEFAULT_MODEL}"
    )

