from database_service.mysql_service import MySQLDatabaseService
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from datetime import datetime

Base = MySQLDatabaseService.get_instance().base

class WorkerSchema(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False, )
    created_at = Column(DateTime, nullable=False, default=datetime())
    updated_at = Column(DateTime, nullable=False)