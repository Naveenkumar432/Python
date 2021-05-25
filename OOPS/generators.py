# Normal method
# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result

# my_nums = square_numbers([1,2,3,4,5])

# print(my_nums)

# Using Generator i.e., yield
def square_numbers(nums):
	for i in nums:
		yield (i*i)

# Generator object
# my_nums = square_numbers([1,2,3,4,5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

my_nums = (x*x for x in [1,2,3,4,5])
#To print all the values use list, It will loose the performance
# print(list(my_nums)

print(my_nums)

for num in my_nums:
	print(num)