class Node:

 def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  
 def __init__(self):
    self.head = None

 def insert_at_head(self, data): # O(1)
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

 def insert_at_end(self, data): # O(n)
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node

 def traverse(self): # O(n)
    current = self.head
    while current:
        print(current.data, end=" -> ")
    print("None")