from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8080
    database_url: str = "postgresql+psycopg2://appdev:111@localhost:5432/agent"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
