import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME, TEMPERATURE

# Load environment variables from .env file
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=os.getenv("GOOGLE_API_KEY")
)