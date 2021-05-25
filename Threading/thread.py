# Threading is use to spead-up program by running diffrent task
# concurrently 

import threading
import time

start = time.time()
# start = time.perf_counter()
# print(start)

def do_something():
	print("sleeping 1 sec...!")
	time.sleep(1)
	print("Done sleep...")

threads = []
for _ in range(10):
	t = threading.Thread(target=do_something)
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# do_something()
# do_something()

finish = time.time()

print(f'Finished in {round(finish-start, 2)} second(s)')