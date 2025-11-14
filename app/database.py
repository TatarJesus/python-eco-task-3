from sqlmodel import create_engine, SQLModel, Session
import os

DB_PATH = os.getenv("GLOSSARY_DB_PATH", "./data/glossary.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# connect_args нужен для SQLite + single-thread
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    # создаёт таблицы, если их ещё нет
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
