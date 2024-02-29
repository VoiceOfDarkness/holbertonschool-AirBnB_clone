"""This module contains City model"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """City model"""

    state_id = ""
    name = ""
