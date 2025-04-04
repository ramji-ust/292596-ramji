import json  # For reading and writing JSON files

# -----------------------
# Person Class
# -----------------------
class Person:
    def __init__(self, name, age, gender):
        # Constructor to initialize common person attributes
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        # Returns a string with personal details
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# -----------------------
# Employee Class (inherits from Person)
# -----------------------
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        # Initialize using the base Person class
        super().__init__(name, age, gender)
        # Add employee-specific attributes
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        # Returns full details including inherited and employee-specific attributes
        return (f"{super().get_details()}, Emp ID: {self.emp_id}, "
                f"Department: {self.department}, Salary: ₹{self.salary:.2f}")

    def is_eligible_for_bonus(self):
        # Returns True if salary is less than ₹50,000
        return self.salary < 50000

    # Method to create Employee from comma-separated string
    def from_string(cls, data_string):
        # Split the string and assign values
        name, age, gender, emp_id, department, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, department, float(salary))
    from_string = classmethod(from_string)  # Convert method to class method

    # Static method to display bonus policy info
    def bonus_policy():
        print("💰 Bonus Policy: Employees earning less than ₹50,000 are eligible for bonuses.")
    bonus_policy = staticmethod(bonus_policy)  # Convert method to static method

    def to_dict(self):
        # Convert employee object to dictionary for saving to JSON
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "emp_id": self.emp_id,
            "department": self.department,
            "salary": self.salary
        }

    def from_dict(data):
        # Create an Employee object from a dictionary (for loading from JSON)
        return Employee(
            data["name"],
            data["age"],
            data["gender"],
            data["emp_id"],
            data["department"],
            data["salary"]
        )
    from_dict = staticmethod(from_dict)  # Convert method to static method


# -----------------------
# Department Class
# -----------------------
class Department:
    def __init__(self, name):
        # Initialize department with a name and empty employee list
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        # Add employee if they are valid and belong to this department
        if isinstance(employee, Employee) and employee.department == self.name:
            self.employees.append(employee)

    def get_average_salary(self):
        # Return 0.0 if no employees, otherwise return average salary
        if not self.employees:
            return 0.0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        # Return a list of employee detail strings
        return [emp.get_details() for emp in self.employees]


# -----------------------
# Persistence Functions
# -----------------------

def save_to_json(employees, filename="employees.json"):
    """
    Save a list of Employee objects to a JSON file using to_dict().
    """
    data = [emp.to_dict() for emp in employees]  # Convert each employee to dictionary
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)  # Write to file with indentation


def load_from_json(filename="employees.json"):
    """
    Load employee data from a JSON file and return a list of Employee objects.
    """
    employees = []
    with open(filename, "r") as f:
        data = json.load(f)  # Load data from file
        for item in data:
            emp = Employee.from_dict(item)  # Convert dict back to Employee object
            employees.append(emp)
    return employees
