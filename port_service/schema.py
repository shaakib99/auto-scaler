from database_service.mysql_service import MySQLDatabaseService
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean
from datetime import datetime

Base = MySQLDatabaseService.get_instance().base

class PortSchema(Base):
    __tablename__ = "ports"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    worker_id = Column(Integer, ForeignKey('workers.id'), nullable=False)
    port_number = Column(Integer, nullable=False)
    port_type = Column(String(255), nullable=True)
    mapped_port = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())