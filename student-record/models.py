from sqlalchemy import Column, Integer, String, Boolean
from students.database import Base, engine



class Student(Base):
    __tablename__ = "record"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    is_present = Column(Boolean, default=True)


