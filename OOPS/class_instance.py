class Employee:
	"""docstring for ClassName"""
	def __init__(self, first, last, pay):
		super(Employee, self).__init__()
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + '.' + self.last + "@company.com"

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('User', 'Test', 60000)

# print("Hello")
print(emp_1.email)
#"shell_cmd": "make"
import sys
print(sys.version)