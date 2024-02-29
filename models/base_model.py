"""This module contains BaseModel model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model to create models"""

    def __init__(self, *args, **kwargs) -> None:
        """
        __init__ - initialization method
        Args:
            args: args
            kwargs: kwargs
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self) -> None:
        """
        save - updates upodated_at argument and saves it to storage
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to__dict - returns the dictionary representation of instance
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self) -> str:
        """
        __str__ - string representation of instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
