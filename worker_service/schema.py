from database_service.mysql_service import MySQLDatabaseService
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, Boolean
from common.enums import WorkerStatusEnum
from datetime import datetime

Base = MySQLDatabaseService.get_base()

class WorkerSchema(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    container_id = Column(String(255), nullable=True)
    ram = Column(Integer, nullable=False, default=512)
    cpu = Column(Integer, nullable=False, default=1)
    status = Column(Enum(WorkerStatusEnum), default=WorkerStatusEnum.INIT)
    parent_id = Column(Integer, ForeignKey('workers.id'), nullable=True)
    is_cloned = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())