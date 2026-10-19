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

provider_settings = {
    "gemini": ("GOOGLE_API_KEY", GEMINI_MODEL, ChatGoogleGenerativeAI),
    "mistral": ("MISTRAL_API_KEY", MISTRAL_MODEL, ChatMistralAI),
    "groq": ("GROQ_API_KEY", GROQ_MODEL, ChatGroq),
}

if DEFAULT_MODEL not in provider_settings:
    raise ValueError(f"Unknown DEFAULT_MODEL: {DEFAULT_MODEL}")

api_key_name, model_name, client_class = provider_settings[DEFAULT_MODEL]
api_key = os.getenv(api_key_name)
if not api_key:
    raise ValueError(f"{api_key_name} is not set for DEFAULT_MODEL={DEFAULT_MODEL}")

llm = client_class(
    model=model_name,
    temperature=MODEL_TEMPERATURE,
    api_key=api_key,
)

