class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def search_by_age(self, target_age):
        result = []
        for employee in self.employees:
            if employee.age == target_age:
                result.append(employee)
        return result
    
    def search_by_name(self, target_name):
        result = []
        for employee in self.employees:
            if employee.name == target_name:
                result.append(employee)
        return result
    
    def search_by_salary(self, operator, target_salary):
        result = []
        for employee in self.employees:
            if operator == '>' and employee.salary > target_salary:
                result.append(employee)
            elif operator == '<' and employee.salary < target_salary:
                result.append(employee)
            elif operator == '>=' and employee.salary >= target_salary:
                result.append(employee)
            elif operator == '<=' and employee.salary <= target_salary:
                result.append(employee)
        return result

def main():
    emp_db = EmployeeDatabase()

    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search by:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        target_age = int(input("Enter the age to search: "))
        result = emp_db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search: ")
        result = emp_db.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the salary operator (<, >, <=, >=): ")
        target_salary = int(input("Enter the target salary: "))
        result = emp_db.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return
    
    if result:
        print("\nSearch results:")
        for employee in result:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
