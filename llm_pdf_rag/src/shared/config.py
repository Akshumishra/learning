import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URL = os.getenv("DB_URL")
    API_KEY = os.getenv("API_KEY")