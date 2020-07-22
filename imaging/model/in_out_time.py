# coding=utf-8

from sqlalchemy import Column, String, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class InOutTime(Base):
    __tablename__ = 'in_out_time'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    in_time = Column(String)
    out_time = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", back_populates="inouttime")

    def __init__(self, date, in_time, out_time, employee):
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.employee = employee
