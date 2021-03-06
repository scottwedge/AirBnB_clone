#!/usr/bin/python3
"""
Unittest for place
"""
import unittest
from datetime import datetime
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """
    Test Place
    """
    def test_right_cases(self):
        """
        right cases
        """
        my_model = Place()
        my_model.name = "Holbi"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holbi")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.__class__.__name__, "Place")
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        my_model.save()
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        my_model_dict = my_model.to_dict()
        self.assertIs(type(my_model_dict), dict)

if __name__ == "__main__":
    unittest.main()
