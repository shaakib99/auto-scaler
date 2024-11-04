from abcs import DatabaseServiceABC
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

class MySQLDatabaseService(DatabaseServiceABC):
    instance = None
    def __init__(self):
        self.engine = create_engine(url=os.getenv('DB_URL'))
        self.session = Session(bind=self.engine, autoflush=False, autocommit=False)
        self.base = declarative_base()

    
    # using singleton pattern to create only single instance
    @staticmethod
    def get_instance() -> "MySQLDatabaseService":
        if MySQLDatabaseService.instance is None:
            MySQLDatabaseService.instance = MySQLDatabaseService()
        return MySQLDatabaseService.instance
    
    @staticmethod
    async def connect():
        db_instance = MySQLDatabaseService.get_instance()
        db_instance.engine.connect()
    
    @staticmethod
    async def disconnect():
        db_instance = MySQLDatabaseService.get_instance()
        db_instance.engine.dispose()

        

    async def create_one(self, data, schema):
        pass

    async def update_one(self, id, data, schema):
        pass

    async def get_one(self, id, schema):
        pass

    async def get_all(self, query, schema):
        pass

    async def delete_one(self, id, schema):
        pass

