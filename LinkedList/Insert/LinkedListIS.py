# created Linked List insertion from start
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def appendStart(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head 
            new_node.next = current
            self.head = new_node
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end = ' --> ')
            current = current.next 
        print('null')
        
ll = LinkedList()
ll.appendStart(10)
ll.appendStart(20)
ll.appendStart(30)
ll.appendStart(40)
ll.appendStart(50)
ll.print()
