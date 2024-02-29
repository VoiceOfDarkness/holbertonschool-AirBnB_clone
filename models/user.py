"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User model"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
