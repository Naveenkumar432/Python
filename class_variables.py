class Employee:
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		super(Employee, self).__init__()
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + '.' + self.last + "@comapany.com"
		Employee.num_of_emps += 1

	def full_name(self):
		return self.first + " " + self.last

	def apply_raise(self):
		# self.pay = int(self.pay * 1.04)
		self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

# print(emp_1.full_name())
# print(emp_2.email)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(Employee.__dict__)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(Employee.num_of_emps)