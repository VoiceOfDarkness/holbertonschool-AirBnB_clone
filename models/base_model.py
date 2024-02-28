from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        from models import storage

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
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
        storage.new(self)

    def save(self) -> None:
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
