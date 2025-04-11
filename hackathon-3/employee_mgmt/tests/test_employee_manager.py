import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        e = self.manager.add_employee("John", "Sales", "Exec", 50000, 5000, 2000)
        self.assertEqual(e.name, "John")
        self.assertAlmostEqual(e.net_salary, 47000.0)

    def test_find_by_id(self):
        e = self.manager.add_employee("Jane", "Marketing", "Lead", 70000, 7000, 3000)
        found = self.manager.find_by_id(e.id)
        self.assertEqual(found.name, "Jane")

    def test_delete_employee(self):
        e = self.manager.add_employee("Tom", "IT", "Support", 40000, 4000, 1000)
        self.assertTrue(self.manager.delete_employee(e.id))
        self.assertIsNone(self.manager.find_by_id(e.id))
