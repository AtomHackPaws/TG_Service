from pydantic_settings import BaseSettings
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = "5431"
    POSTGRES_DATABASE: str
    TELEGRAM_BOT_TOKEN: str
    MINIO_LINK: str
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_BUCKET: str
    CHANNEL_ID: int
    KAFKA_URL: str = ""

    class Config:
        env_file = ".env"

    @property
    def database_settings(self) -> dict:
        return {
            "database": self.POSTGRES_DATABASE,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }
    
    
    @property
    def s3_url(self) -> dict:
        return self.MINIO_LINK + '/' + self.MINIO_BUCKET

    @property
    def database_uri_async(self) -> str:
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )


settings = Settings()
bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
