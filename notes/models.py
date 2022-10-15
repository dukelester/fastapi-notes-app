""" The notes application models and tables """

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base

class Notes(Base):
    """ The model for the notes table """
    __tablename__="notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(100),nullable=False, index=True)
    description = Column(String(200),index=True)
    created_date = Column(DateTime, default=func.now(), nullable=False)
