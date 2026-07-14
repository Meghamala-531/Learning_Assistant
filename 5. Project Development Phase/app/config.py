import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
LOCAL_MODEL_NAME = os.getenv("LOCAL_MODEL_NAME", "MBZUAI/LaMini-Flan-T5-77M").strip()
HOST = os.getenv("HOST", "127.0.0.1").strip()
PORT = int(os.getenv("PORT", "8000").strip())
