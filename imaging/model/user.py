# coding=utf-8
import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    active = Column(Integer, default=1)
    create_date = Column(String, default=datetime.datetime.utcnow)
    employee = relationship("Employee", uselist=False, backref="user")

    def __init__(self, name, login, password, active):
        self.name = name
        self.login = login
        self.password = password
        self.active = active
