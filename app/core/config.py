import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")