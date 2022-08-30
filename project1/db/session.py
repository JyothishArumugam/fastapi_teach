from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

SQLAlchemy_DB_URL = "sqlite:///./sql_app.db"
engine= create_engine(SQLAlchemy_DB_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False,
                            autoflush= False, 
                            bind =engine
                            
                            )
def get_db()-> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()