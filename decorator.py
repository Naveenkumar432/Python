class Employee:
	raise_amt = 1.04

	def __init__(self, first, last):
		self.first = first
		self.last = last
		# self.email = self.first + '.' + self.last + "@company.com"

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)
	
	@property
	def full_name(self):
		return "{} {}".format(self.first, self.last)

	@full_name.setter
	def full_name(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@full_name.deleter
	def full_name(self):
		print("Delete Name!")
		self.first = None
		self.last = None

emp_1 = Employee("John", "Smith")
# print(emp_1.full_name())
emp_1.full_name = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)
del emp_1.full_name