from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os


class DatabaseManager():
    
    def __init__(self, database_path="data/users.db"):
        # Create a directory for the database if it doesn't exist
        os.makedirs(os.path.dirname(database_path), exist_ok=True)
        
        # Create the db engine for managing db connections
        self.engine = create_engine(f"sqlite:///{database_path}", echo=True)

        # Create session factory
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_tables(self):
        #Create all tables defined in the models
        Base.metadata.create_all(self.engine)
        print("Tables created successfully.")

    def get_session(self):
        # Get a database session
        return self.SessionLocal()