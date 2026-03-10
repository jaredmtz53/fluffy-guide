from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    NEON_CONNECTION_STRING: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str
    ALGORITHM: str
    RESEND_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

