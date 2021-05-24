# my_list = [1, 2,3,4,5]
# new_list = list(map(lambda x : x*x, my_list))
# print(new_list)

# t = 'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759'
# import os
# print(os.path.split(t))
# t.split("/")
# print(t)

# txt = "hello, my name is Peter, I am 26 years old"

# x = txt.split(", ")

# print(x)
# a = "1\\2\\3\\4"
# print(a.split('\\'))

# name = '/stack/overflow'
# name.split("/")
# print(name)

# ^^^^^^^^^^^^^^^^^^^^^ZIP^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# coordinate = ['x', 'y', 'z']
# value = [3, 4, 5]
# result = zip(coordinate, value)
# # print(result)

# result_list = list(result)
# # print(result_list)
# c,v = zip(*result_list)
# print(c)
# print(v)

# ^^^^^^^^^^^^^^^^^^^MAP^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# my_list = [1,2,3,4,5]
# new_list = list(map(lambda x: x*2, my_list))
# print(new_list)

#^^^^^^^^^^^^^^^^^^^^REDUCE^^^^^^^^^^^^^^^^^^^^^^^^^
from functools import reduce

li = [5,8,10,20,50,100]
sum = reduce(lambda x,y: x+y, li)
print(sum)
# print(len(li))