# Exercise 5: Thread-Safe Linked List Implementation
# --------------------------------------------------
# This custom linked list enforces a max size and uses thread locks for safe
# concurrent appends. Review this as a systems developer for performance,
# memory efficiency, and potential race conditions or data structure improvements.



import threading

class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
   def __init__(self, max_size=None):
       self.head = None
       self.size = 0
       self.max_size = max_size
       self.lock = threading.Lock()

   def append(self, data):
       # Validate input data
       if len(data) > 1000:
           raise ValueError("Data size exceeds maximum limit")
           
       with self.lock:
           if self.max_size is not None and self.size >= self.max_size:
               raise ValueError("Linked list is full")
           
           new_node = Node(data)
           if self.head is None:
               self.head = new_node
           else:
               last = self.head
               while last.next:
                   last = last.next
               last.next = new_node
           self.size += 1

   def print_list(self):
       current = self.head
       while current:
           print(current.data, end=" ")
           current = current.next
