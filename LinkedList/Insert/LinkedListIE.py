# Created Linked List insertion from end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def append(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_data
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end = ' --> ')
            current = current.next
        print('null')
        
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print()
