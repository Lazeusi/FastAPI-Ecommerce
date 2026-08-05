from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )
    
    app_name: str
    app_version: str
    debug: bool
    
    host: str
    port: int
    
settings = Settings()