# Queue: FIFO: First In First-Out
# Enqueue: add an item to the end of the line
# Dequeue: remove an item from the front of the line
# Enque from one end, and Dequeue from other end

# we need to import deque from modle collections

# We use append() to enqueue an item, and popleft() to dequeue an item.

# Example

from collections import deque
# my_queue = deque()
# my_queue.append(5)
# my_queue.append(10)
# print(my_queue)
# print(my_queue.popleft())

#Wrapper class for Queue
class Queue():
	def __init__(self):
		self.queue = deque()

	def push(self, item):
		self.queue.append(item)

	def pop(self):
		if len(self.queue) > 0:
			return self.queue.popleft()
		else:
			return None

	def __str__(self):
		return str(self.queue)

my_queue = Queue()
my_queue.push(5)
my_queue.push(10)
print(my_queue)
print(my_queue.pop())