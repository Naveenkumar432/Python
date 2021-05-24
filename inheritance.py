class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + '.' + self.last + "@company.com"

	def full_name(self):
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		# super(Employee, self).__init()
		# super(Employee, self).__init__()
		# Employee.__init__(self,first,last,pay)
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print("-->",emp.full_name())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 40000, [dev_1])
# print(help(Developer))
# print(dev_1.full_name())
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.email)
# print(dev_1.prog_lang)
# print(mgr_1.email)
# mgr_1.print_emp()	

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))