from collections.abc import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

from src.config import settings
from src.constants import DB_NAMING_CONVENTION

DATABASE_URL = str(settings.DATABASE_URL)

metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)
engine = create_engine(DATABASE_URL, echo=settings.DEBUG, pool_size=10, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
