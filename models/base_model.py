from uuid import uuid4
from datetime import date, datetime


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now() 
        self.updated_at = datetime.now()

    def save(self) -> None:
        self.updated_at = datetime.now()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
