from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "Tech5@fdjnofox#"
    ALGORITHM: str = "HS256"

    class Config:
        case_sensitive = True

settings = Settings()
