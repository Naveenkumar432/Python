# import time

# import multiprocessing

# start = time.time()

# def do_something():
# 	print("Sleeping for 1 sec....!")
# 	time.sleep(1)
# 	print("Done sleep....!")

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# finish = time.time()

# print(f'finished in {round(finish-start, 2)} second(s)')





import multiprocessing
print(dir(multiprocessing))
import time

start = time.time()
# start = time.perf_counter()
# print(start)

def do_something():
	print("sleeping 1 sec...!")
	time.sleep(1)
	print("Done sleep...")

# threads = []
# for _ in range(10):
# 	t = threading.Thread(target=do_something)
# 	t.start()
# 	threads.append(t)

# for thread in threads:
# 	thread.join()

t1 = multiprocessing.Process(target=do_something)
t2 = multiprocessing.Process(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()
# do_something()
# do_something()

finish = time.time()

print(f'Finished in {round(finish-start, 2)} second(s)')