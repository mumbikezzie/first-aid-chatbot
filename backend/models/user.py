from datetime import date
import uuid
from sqlalchemy import Boolean,String,Column, Date, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from db.base_class import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4())
    first_name = Column(String(length=256), nullable=False)
    last_name = Column(String(length=256), nullable=False)
    email = Column(String(length=256), unique=True, nullable=False)
    password = Column(String(length=256), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    created_ts = Column(Date, default=func.current_date(), nullable=True)
    updated_ts = Column(Date, onupdate=func.current_date(), nullable=True)