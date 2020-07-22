# coding=utf-8

from sqlalchemy import Column, BLOB, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class EmployeeImage(Base):
    __tablename__ = 'employee_image'

    id = Column(Integer, primary_key=True)
    image = Column(BLOB)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", back_populates="employeeimage")

    def __init__(self, image, employee):
        self.image = image
        self.employee = employee
