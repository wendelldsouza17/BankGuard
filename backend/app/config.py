from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "BankGuard"
    debug: bool = True


settings = Settings()