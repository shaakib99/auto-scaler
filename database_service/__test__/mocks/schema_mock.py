from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

MockBase = declarative_base()

class MockSchema(MockBase):
    __tablename__ = "test"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)