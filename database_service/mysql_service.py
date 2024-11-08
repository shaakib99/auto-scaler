from .abcs import DatabaseServiceABC
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, DeclarativeBase, load_only, joinedload
from pydantic import BaseModel
from common.models import Query
import os

class MySQLDatabaseService(DatabaseServiceABC):
    instance = None
    def __init__(self):
        self.engine = create_engine(url=os.getenv('DB_URL'))
        self.session = Session(bind=self.engine, autoflush=False, autocommit=False)
        self.base = declarative_base()
        self.base.metadata.create_all()

    
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

        

    async def create_one(self, data: BaseModel, schema: DeclarativeBase):
        data_model = schema(**data.model_dump())
        self.session.add(data_model)
        self.session.commit()
        return data_model

    async def update_one(self, id, data: BaseModel, schema: DeclarativeBase):
        data_model = self.get_one(id, schema)
        for key, value in data.model_dump():
            setattr(data_model, key, value)
        self.session.commit()
        return data_model

    async def get_one(self, id, schema: DeclarativeBase):
        return self.session.get_one(schema, id)

    async def get_all(self, query: Query, schema: DeclarativeBase):
        cursor = self.session.query(schema)
        if query.selected_fields:
            columns = [getattr(schema, field) for field in query.selected_fields]
            cursor = cursor.options(load_only(*columns))

        for field in query.join:
            relationship_attr = getattr(schema, field)
            cursor = cursor.options(joinedload(relationship_attr))

        if query.filter_by:
            cursor = cursor.where(text(query.filter_by))
        if query.group_by:
            cursor = cursor.group_by(text(query.group_by))
        if query.having:
            cursor = cursor.having(text(query.having))
        if query.order_by:
            cursor = cursor.order_by(text(query.order_by))
        
        cursor = cursor.limit(query.limit)
        cursor = cursor.offset(query.skip)

        if len(query.selected_fields):
            return [res.__dict__ for res in cursor.all()]

        return cursor.all()

    async def delete_one(self, id, schema: DeclarativeBase):
        data = self.get_one(id, schema)
        self.session.delete(data)
        self.session.commit()

