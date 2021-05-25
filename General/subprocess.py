# Caling exteranl command using python with subprocess module
import subprocess
#print(dir(subprocess))
# subprocess.run(['dir'], shell=True) # For Windows

# subprocess.run('ls') # For linux

#To add muliple commands use list
# subprocess.run(['ls', '-la'])

# To capture the output in a variable

# p1 = subprocess.run(['ls', '-la'])
# print(p1)

p1 = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
# It will give the args passed in subprocess
#print(p1.args)
# If it reurns zero our code executed successfully
#print(p1.returncode)

# To grab std out
#print(p1.stdout.decode())
#print(p1.stdout)

# capture_output sets the stdout and std error to subprocess PIPE
# We can use instead
# p1 = subprocess.run(['dir'], shell=True, stdout=subprocess.PIPE, text=True)
# print(p1.stdout)

# Redirect output to other places Ex: To a file
# with open('E:/General/output.txt', 'w') as f:
# 	p1 = subprocess.run(['dir'], shell=True, stdout=f, text=True)


# p1 = subprocess.run(['dir', 'dne'], shell=True, stderr=subprocess.DEVNULL)
# print(p1.stdout)


# Output of one commad into input of another command
p1 = subprocess.run(['type', 'test.txt'], shell=True, capture_output=True, text=True)
print(p1.stdout)