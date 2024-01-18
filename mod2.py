class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = (overtime_hours * (self.emp_salary / 50))
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary

        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

# Taking employee data from user input
employees_data = []
for _ in range(4):
    emp_name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    emp_salary = float(input("Enter employee salary: "))
    emp_department = input("Enter employee department: ")
    
    employees_data.append((emp_name, emp_id, emp_salary, emp_department))

# Creating instances of Employee class
employees = [Employee(*data) for data in employees_data]

# Using the methods
for emp in employees:
    print("\n")
    emp.print_employee_details()
    new_department = input("Enter the new department: ")
    emp.emp_assign_department(new_department)
    hours_worked = float(input("Enter the hours worked: "))
    total_salary = emp.calculate_emp_salary(hours_worked)
    print("Total Salary:", total_salary)
    print("\n")
