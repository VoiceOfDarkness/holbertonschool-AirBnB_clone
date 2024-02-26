from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self) -> None:
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        return result

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
