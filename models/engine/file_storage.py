#!/usr/bin/python3
"""This reprenets a module which is the file storage class"""
import json
import os
import datetime


class FileStorage():
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    # def __init__(self):
    #     pass

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''this set in __objects the obj with key <obj class name>.id'''
        obj_name = obj.__class__.__name__
        obj_ID = obj.id
        key = f"{obj_name}.{obj_ID}"  # <class name>.id = obj
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        # serialize the object by first converting it to a dictionary
        object_dict = {}

        for key in self.__objects.keys():
            if type(self.__objects[key]) != dict:
                object_dict[key] = self.__objects[key].to_dict()
        # convert the dictionary object to json and write to the file
        my_file_name = self.__file_path
        with open(my_file_name, "w", encoding="utf-8") as jsonfile:
            # json.dump(object_dict, jsonfile)
            jsonfile.write(json.dumps(object_dict))

    def reload(self):
        """Reloads the stored objects"""
        if os.path.exists(FileStorage.__file_path):
            #  load the file and dump content as dictionary
            with open(FileStorage.__file_path, "r", encoding="utf-8") \
                    as my_file:
                object_dict = json.loads(my_file.read())
            final_dict = {}

            for id, dictionary in object_dict.items():
                class_name = dictionary['__class__']
                final_dict[id] = self.classes()[class_name](**dictionary)
            FileStorage.__objects = final_dict
