from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
# conexão local - MySQL
engine = create_engine(DATABASE_URL) 

# conexão supabase - PostgreSQL
#engine = create_engine("postgresql://postgres:password@db.project.supabase.co:5432/postgres")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()
