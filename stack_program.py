# Assessment 3.2: Stack (LIFO) Dynamic Program
# File name: stack_program.py

# 1. Create an empty stack.
stack = []

# 2. Push S, E, L, L, L, O, N onto the stack in that order.
letters = ['S', 'E', 'L', 'L', 'L', 'O', 'N']
for letter in letters:
    stack.append(letter)

# 3. Display the stack from bottom to top.
print(" ".join(stack))

# 4. While the stack is not empty, pop the top letter and display the remaining stack.
while len(stack) > 0:
    stack.pop()
    if len(stack) > 0:
        print(" ".join(stack))
    else:
        print("Empty")