# Assessment 3.2: Linked List Dynamic Program
# File name: linked_list_program.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        if not self.head:
            print("Empty")
            return
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" → ".join(elements))

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

# --- Main Execution ---
# 1. Create an empty linked list.
ll = LinkedList()

# 2. Add a node for each letter in SELLLON, in order.
letters = ['S', 'E', 'L', 'L', 'L', 'O', 'N']
for letter in letters:
    ll.append(letter)

# 3. Display the linked list.
ll.display()

# 4. While the linked list is not empty, delete the last node and display the remaining list.
while ll.head is not None:
    ll.delete_last()
    ll.display()