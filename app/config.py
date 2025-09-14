from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_SITE: str
    model_config = SettingsConfigDict(
        env_file=(Path(__file__) / ".." / ".env").resolve()
    )

    def get_webhook_url(self) -> str:
        return f"{self.BASE_SITE}/webhook"
