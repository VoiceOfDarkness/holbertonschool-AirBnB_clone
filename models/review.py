"""This module contains Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
