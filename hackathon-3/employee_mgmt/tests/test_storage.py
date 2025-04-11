import unittest
import os
import pickle
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.file = "test_employees.pkl"
        self.storage = Storage(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_save_and_load(self):
        data = [
            {
                "id": "1",
                "name": "Anna",
                "department": "Finance",
                "designation": "Analyst",
                "gross_salary": 70000,
                "tax": 10000,
                "bonus": 3000,
                "net_salary": 63000
            }
        ]
        self.storage.save(data)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "Anna")
