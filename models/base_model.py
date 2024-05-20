#!/usr/bin/python3
"""
base_model.py: defines the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all future classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the instance with attributes
        provided in kwargs, if any"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
             for key, value in kwargs.items():
                # convert to datetime
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Parse datetime attributes from string format
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Provide a readable representation of the instance"""
        Basemodel = self.__class__.__name__
        return f"[{Basemodel}] ({self.id}) {self.__dict__}"
        """The following line is an alternative
        implementation, kept for reference"""
        """return "[{:s}] ({:s}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)"""

    def save(self):
        """Update the updated_at timestamp to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the instance to a dictionary,
        formatting dates as ISO 8601 strings"""
        new_dict = self.__dict__.copy()
        self.created_at = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        new_dict['created_at'] = self.created_at
        new_dict['updated_at'] = self.updated_at
        new_dict['__class__'] = self.__class__.__name__
        return new_dict


if __name__ == "__main__":
    # Create an instance of BaseModel and print its string representation
    base_instance = BaseModel()
    print(base_instance)
