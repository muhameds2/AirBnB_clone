"""unit test for base_model module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """tests for BaseModel class"""

    def setUp(self):
        """init BaseModel inst"""
        self.base_inst = BaseModel()

    def test_initialization(self):
        """Testing initialization"""
        self.assetIsInstance(self.base_inst.id, str)
        self.assertIsInstance(self.base_inst.created_at, datetime)
        self.assertIsInstance(self.base_inst.updated_at, datetime)

    def test_str(self):
        """test method for str rep"""
        expec_str = f"[BaseModel] ({self.base_inst.id}) {self.base_inst.__dict__}"
        self.assertEqual(str(self.base_inst), expec_str)

    def test_save_method(self):
        """testing for save method"""
        prev_updated = self.base_inst.updated_at
        self.base_inst.save()
        self.assertNotEqual(prev_updated, self.base_inst.updated_at)

    def test_to_dict_method(self):
        """test method for dict"""
        base_dict = self.base_inst.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertIn('__class__', base_dict)

    if __name__ == '__main__':
        unittest.main()
