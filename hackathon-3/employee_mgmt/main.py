# main.py

from employee_manager import EmployeeManager
from storage import Storage

def display_employees(employees):
    if not employees:
        print("No employees found.")
    for e in employees:
        print(f"{e.id} - {e.name}, Dept: {e.department}, Designation: {e.designation}, Net Salary: {e.net_salary:.2f}")

def main():
    manager = EmployeeManager()
    storage = Storage()

    saved_data = storage.load()
    manager.load_employees(saved_data)

    while True:
        print("\n1. Add Employee\n2. View All\n3. Search by ID\n4. Delete Employee\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            dept = input("Department: ")
            desig = input("Designation: ")
            gross = input("Gross Salary: ")
            tax = input("Tax: ")
            bonus = input("Bonus: ")
            emp = manager.add_employee(name, dept, desig, gross, tax, bonus)
            storage.save(manager.to_dict_list())
            print(f"Employee added with ID: {emp.id}")

        elif choice == '2':
            display_employees(manager.get_all_employees())

        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            emp = manager.find_by_id(emp_id)
            if emp:
                print(f"{emp.id} - {emp.name}, Dept: {emp.department}, Designation: {emp.designation}, Net Salary: {emp.net_salary:.2f}")
            else:
                print("Employee not found.")

        elif choice == '4':
            emp_id = input("Enter Employee ID: ")
            if manager.delete_employee(emp_id):
                storage.save(manager.to_dict_list())
                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
