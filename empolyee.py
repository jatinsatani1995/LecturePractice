class employee: 
    
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department
        
    def assign_department(self, emp_department):
            self.department = emp_department
        
    def calculate_salary(self,salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
            self.salary = salary + (overtime * (self.salary / 50))
      
    def employee_details(self):
        print("\n Employee Name: ", self.name)
        print("Employee ID: ", self.id)
        print("Employee Salary: ", self.salary)
        print("Employee Department: ", self.department)
       
        
       
employee1 = employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = employee("MARTIN", "E7900", 50000, "SALES")
employee4 = employee("SMITH", "E7698", 55000, "OPERATIONS")

employee1.employee_details()
employee2.employee_details()
employee3.employee_details()
employee4.employee_details()


employee1.assign_department("Marketting")
employee2.assign_department("Production")


employee1.employee_details()
employee2.employee_details()
employee3.employee_details()
employee4.employee_details()

employee1.calculate_salary(55000,51)
employee1.employee_details()  