import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Config(BaseModel):
    """Configuration settings loaded from environment variables."""
    
    # LinkedIn Configuration
    LINKEDIN_POST_ID: str = os.getenv("LINKEDIN_POST_ID", "")
    LINKEDIN_ACCESS_TOKEN: str = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
    LINKEDIN_USER_ID: str = os.getenv("LINKEDIN_USER_ID", "")
    
    # LLM Configuration
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    
    # Game Configuration
    SYSTEM_PROMPT: str = os.getenv("SYSTEM_PROMPT", "")
    RESPONSE_TEMPERATURE: float = float(os.getenv("RESPONSE_TEMPERATURE", "0.7"))
    GAME_PASSWORD: str = os.getenv("GAME_PASSWORD", "")


config = Config() 