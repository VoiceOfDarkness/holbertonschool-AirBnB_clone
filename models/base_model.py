from uuid import uuid4
from datetime import date, datetime


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
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

    def save(self) -> None:
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        return result

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
