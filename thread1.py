# We will see how to pass args to a function i.e., list of args

import threading
import time

start = time.time()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)...!")
	time.sleep(seconds)
	print("Done sleep...")

threads = []
for _ in range(10):
	t = threading.Thread(target=do_something, args=[1.5])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()


finish = time.time()

print(f'Finished in {round(finish-start, 2)} second(s)')