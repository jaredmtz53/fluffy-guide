from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    NEON_CONNECTION_STRING: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()