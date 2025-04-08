"""Module for creating database connections"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = "postgresql://" \
    f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"\
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}"\
    f"/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
