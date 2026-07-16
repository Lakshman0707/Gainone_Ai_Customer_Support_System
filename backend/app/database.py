from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import *

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}"
    f"/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()