import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        # Initialize the instance with attributes provided in kwargs, if any

        if kwargs is not None:
            for key, value in kwargs.items():
                # Skip the __class__ attribute to avoid conflicts
                if key == "__class__":
                    continue
                # Parse datetime attributes from string format
                if key == "created_at":
                    setattr(self, "created_at", datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    setattr(self, "updated_at", datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        """Assign a unique ID, turn it into a
        string format and initialize timestamps
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        # Provide a readable representation of the instance
        Basemodel = self.__class__.__name__
        return f"[{Basemodel}] ({self.id}) {self.__dict__}"
        """The following line is an alternative
        implementation, kept for reference"""
        """return "[{:s}] ({:s}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)"""

    def save(self):
        # Update the updated_at timestamp to the current time
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
