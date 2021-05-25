# Threadpool executor easier and more efficient way to run threads and it also allows to switch multiple processes instead of threads as well
# depending on the problem we trying to solve 

import concurrent.futures
import time 

start = time.time()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)...!")
	time.sleep(seconds)
	return f"Done sleep {seconds}..."

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]

	# We can use map function
	results = executor.map(do_something, secs)

# If we want to handle exception we need to handle it in iterator
	for result in results:
		print(result)
	# results = [executor.submit(do_something, sec) for sec in secs]

	# for f in concurrent.futures.as_completed(results):
	# 	print(f.result())

	# f1 = executor.submit(do_something, 1)
	# f2 = executor.submit(do_something, 1)

	# print(f1.result())
	# print(f2.result())


finish = time.time()

print(f'Finished in {round(finish-start, 2)} second(s)')