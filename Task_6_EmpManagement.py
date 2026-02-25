# Base Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        # This method will be overridden
        return self.base_salary


# Subclass: Regular Employee
class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # Regular employees get base salary + bonus
        return self.base_salary + self.bonus


# Subclass: Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        # Paid per hour
        return self.hourly_rate * self.hours_worked


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        # Managers get base salary + allowance + 10% performance bonus
        performance_bonus = self.base_salary * 0.10
        return self.base_salary + self.allowance + performance_bonus


# Polymorphism in action
employees = [
    RegularEmployee("Tom", 3000, 500),
    ContractEmployee("Tim", 20, 160),
    Manager("Brain", 5000, 1000)
]

for emp in employees:
    print(f"{emp.name}'s Salary: ${emp.calculate_salary()}")