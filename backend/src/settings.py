from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 5000
    database_url: str = "sqlite:///db/db.sqlite3"

settings = Settings()