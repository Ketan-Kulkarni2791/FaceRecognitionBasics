# coding=utf-8
import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    active = Column(Integer, default=1)
    create_date = Column(String, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    inouttime = relationship("InOutTime", back_populates="employee")
    employeeimage = relationship("EmployeeImage", back_populates="employee")

    def __init__(self, name, code, active, user):
        self.name = name
        self.code = code
        self.active = active
        self.user = user
