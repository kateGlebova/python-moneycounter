from sqlalchemy import Column, Integer, DateTime, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Date(Base):
    """
    Dates table schema.
    """
    __tablename__ = 'dates'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    operations = relationship("Operation", back_populates="date")

    def __str__(self):
        return self.date.strftime('%d %b %Y')


class Operation(Base):
    """
    Operations table schema.
    """
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    money = Column(Float(asdecimal=True), nullable=False)
    date_id = Column(Integer, ForeignKey('dates.id'), nullable=False)

    date = relationship("Date", back_populates="operations")

    @classmethod
    def get_balance(cls, session):
        return sum([operation.money for operation in session.query(cls).all()])

    def __str__(self):
        return str(self.date) + "\t" + self.description + "\t" + "%.2f" % self.money
