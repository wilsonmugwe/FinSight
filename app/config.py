import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()


class Settings:
    def __init__(self) -> None:
        # General
        self.APP_NAME: str = os.getenv("APP_NAME", "FinSight")
        self.APP_ENV: str = os.getenv("APP_ENV", "development")

        # Database
        self.DATABASE_URL: str = os.getenv(
            "DATABASE_URL",
            "postgresql+psycopg2://postgres:password@localhost:5432/finsight_db",
        )

        # Security / JWT
        self.JWT_SECRET_KEY: str = os.getenv(
            "JWT_SECRET_KEY", "change_this_secret_key"
        )
        self.JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
        self.JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
            os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "60")
        )

        # AI provider
        self.OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


# Single settings instance imported everywhere
settings = Settings()
