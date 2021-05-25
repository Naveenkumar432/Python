#https://docs.python.org/3/reference/datamodel.html#special-method-names

class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + "@gmail.com"
		self.pay = pay

	def full_name(self):
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return "{} - {}".format(self.full_name, self.email)

	# By adding employees it returns total pay 
	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.full_name())

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

# print(emp_1 + emp_2)
# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))

# print('test'.__len__())
print(len(emp_1))