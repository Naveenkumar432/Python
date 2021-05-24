# Closures
# def outer_function(msg):
# 	def inner_function():
# 		print(msg)
# 	return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# Decorator is a function that takes another function as an argument 
# adds some kind of functionality and then returns another function
# all of these without altering the source code of the original function
# that is passes in.

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("Wrapper executed before {}".format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print("display function ran")
# decorated_display = decorator_function(display)
# decorated_display()
# display = decorator_function(display)
# display()

@decorator_function
def display_info(name, age):
	print("display_info ran with arguments ({}, {})".format(name,age))
# display_info('John', 25)


#Class as decorator

# class decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print("call executed before {}".format(self.original_function.__name__))
# 		return self.original_function(*args, **kwargs)

# @decorator_class
# def display():
# 	print("display function ran")

# # display()

# @decorator_class
# def display_info(name, age):
# 	print("display_info ran with arguments ({}, {})".format(name,age))
# display_info('John', 25)