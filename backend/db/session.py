from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import settings
from settings.config import settings

"""
To start talking to our database, the ORM's handle to the database is the Session
"""
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI_POSTGRES, pool_size=60, max_overflow=0)
# engine = create_engine(settings.SQLALCHEMY_DATABASE_URI_POSTGRES)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
conn = SessionLocal()