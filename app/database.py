from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

# Base class for ORM models
Base = declarative_base()

# Database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,   # set to True to see SQL in console
    future=True,
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency for FastAPI routes.
    Yields a database session and ensures it is closed afterwards.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
