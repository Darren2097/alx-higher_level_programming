#!/usr/bin/python3
"""contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """City class inherited from Base"""

    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('state.id'))
