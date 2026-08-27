from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BankGuard"
    debug: bool = True
    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/bankguard"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()