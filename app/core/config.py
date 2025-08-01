import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI App")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
