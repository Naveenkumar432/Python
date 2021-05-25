import os
# print(os.getcwd())
os.chdir("C:/Users/User/Desktop")
# print(os.getcwd())

# os.mkdir('Naveen-3')
# os.makedirs('Naveen/naveen-2')
# os.rmdir('Naveen-3')
# os.removedirs('Naveen/naveen-2')

# os.rename('test.py', 'demo.py')
print(os.listdir())

# for dirPath, dirName, filenames in os.walk("C:/Users/User/Desktop"):
# 	print (dirPath)
# 	print (dirName)
# 	print(filenames)

# print(os.environ.get('HOME'))
# print(os.environ)
file_path = os.path.join(os.environ.get('USERPROFILE'), 'text.txt')
# print(file_path)
# with open(file_path, 'w') as f:
# 	f.write("Test file")
# with open(file_path, 'r') as f:
# 	print(f.read())
# print(os.path.basename('C:\\Users\\User\\text.txt'))
# print(os.path.dirname('C:\\Users\\User\\text.txt'))
# print(os.path.split('C:\\Users\\User\\text.txt'))
# print(os.path.exists('C:\\Users\\User\\text.txt'))
# print(os.path.isdir('C:\\Users\\User\\text.txt'))
# print(os.path.isfile('C:\\Users\\User\\text.txt'))
# print(os.path.splitext('C:\\Users\\User\\text.txt'))
print(dir(os.path))