# Difference between Regular method, class method and static method
# Class and Regular method automatically takes instance as first argument, by convention we call it as self or cls.
# class methods are alternative constrructor

class Employee:
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		# super(Employee, self).__init__()
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + '.' + self.last + "@comapany.com"
		Employee.num_of_emps += 1

	def full_name(self):
		return self.first + " " + self.last

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last,pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_weekday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

# Employee.set_raise_amt(1.05)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# Alternative to this is class method i.e.,Ex: from_string method
# first, last, pay = emp_str_1.split('-')
# print(first, last, pay)
#new_emp_1 = Employee(first, last,pay)

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

import datetime
my_date = datetime.datetime(2018, 7, 15)

print(Employee.is_weekday(my_date))