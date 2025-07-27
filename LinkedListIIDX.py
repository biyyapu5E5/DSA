# Creatd Linked List insertion at particular Index
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def append(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_data
        self.length += 1
    
    def appendIndex(self, index, data):
        if index < 0 or index >= self.length:
            print(f'Enter a b/w number>=0 and number<={self.length - 1}')
            return
           
        current = self.head
        new_data = Node(data)
        
        if index == 0:
            new_data.next = self.head
            self.head = new_data

        else:
            count = 0
            while count < index:
                current = current.next
                count+=1
            new_data.next = current.next
            current.next = new_data
        self.length+= 1
        self.displayList()
            
    def displayList(self):
        current = self.head 
        while current:
            print(current.data, end= ' --> ')
            current = current.next 
        print('null')
        
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print('List of Items: ')
ll.displayList()
ll.appendIndex(2, 67)
ll.appendIndex(9, 18)
ll.appendIndex(4, 28)
ll.appendIndex(0, 18)
