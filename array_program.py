# Assessment 3.2: Array Dynamic Program
# File name: array_program.py

# 1. Create an empty array.
array_data = []

# 2. Add the letters S, E, L, L, L, O, N to the array.
letters = ['S', 'E', 'L', 'L', 'L', 'O', 'N']
for letter in letters:
    array_data.append(letter)

# 3. Display the array.
print(" ".join(array_data))

# 4. While the array is not empty, remove the last letter and display the remaining array.
while len(array_data) > 0:
    array_data.pop()
    if len(array_data) > 0:
        print(" ".join(array_data))
    else:
        print("Empty")