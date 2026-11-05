# Assessment 3.2: Queue (FIFO) Dynamic Program
# File name: queue_program.py

from collections import deque

# 1. Create an empty queue.
queue = deque()

# 2. Enqueue S, E, L, L, L, O, N in that order.
letters = ['S', 'E', 'L', 'L', 'L', 'O', 'N']
for letter in letters:
    queue.append(letter)

# 3. Display the queue from front to rear.
print(" ".join(queue))

# 4. While the queue is not empty, dequeue the front letter and display the remaining queue.
while len(queue) > 0:
    queue.popleft()
    if len(queue) > 0:
        print(" ".join(queue))
    else:
        print("Empty")