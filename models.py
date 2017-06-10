from sqlalchemy import Column, Integer, DateTime, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Date(Base):
    __tablename__ = 'dates'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    operations = relationship("Operation")


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    money = Column(Float(asdecimal=True))
    date_id = Column(Integer, ForeignKey('dates.id'))
