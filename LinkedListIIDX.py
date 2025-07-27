# Creatd Linked List insertion at particular Index
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
    
    def appendIndex(self, index, data):
        current = self.head
        new_data = Node(data)
        count = 1 
        while count <= index:
            if count == index:
                new_data.next = current.next
                current.next = new_data
            count+=1 
            current = current.next
            
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
ll.appendIndex(2, 50)
ll.print()
ll.appendIndex(5, 90)
ll.print()
        
