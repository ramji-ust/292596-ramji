# employee_manager.py

from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee

    def get_all_employees(self):
        return self.employees

    def find_by_id(self, emp_id):
        return next((e for e in self.employees if e.id == emp_id), None)

    def delete_employee(self, emp_id):
        employee = self.find_by_id(emp_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(d) for d in employee_dicts]

    def to_dict_list(self):
        return [e.to_dict() for e in self.employees]
