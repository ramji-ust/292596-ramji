import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_create_employee(self):
        e = Employee("Alice", "HR", "Manager", 80000, 12000, 5000)
        self.assertEqual(e.name, "Alice")
        self.assertEqual(e.department, "HR")
        self.assertEqual(e.designation, "Manager")
        self.assertEqual(e.gross_salary, 80000)
        self.assertEqual(e.tax, 12000)
        self.assertEqual(e.bonus, 5000)
        self.assertAlmostEqual(e.net_salary, 73000.0)

    def test_dict_conversion(self):
        e = Employee("Bob", "IT", "Engineer", 60000, 10000, 2000)
        d = e.to_dict()
        e2 = Employee.from_dict(d)
        self.assertEqual(e.id, e2.id)
        self.assertEqual(e2.name, "Bob")
        self.assertAlmostEqual(e2.net_salary, 52000.0)
