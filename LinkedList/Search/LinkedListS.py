# Created LinkedList to search an element.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def appendItem(self, data):  
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_data
    
    def findItem(self, data):
        findItemIndex = []
        if self.head is None:
            print(findItemIndex)
            return 
        else:
            current = self.head
            index = 0
            while current:
                if current.data == data:
                    findItemIndex.append(index)
                index+=1
                current = current.next
        print('Not Found' if len(findItemIndex) == 0 else findItemIndex)
    
    def displayList(self):
        current = self.head 
        while current:
            print(current.data, end = ' --> ')
            current = current.next
        print('null')
            
            
ll = LinkedList()
ll.appendItem(10)
ll.appendItem(-20)
ll.appendItem(10)
ll.appendItem(20)
ll.appendItem(10)
ll.displayList()
ll.findItem(10)
ll.findItem(20)
ll.findItem(30)

# Output
# 10 --> -20 --> 10 --> 20 --> 10 --> null
# [0, 2, 4]
# [3]
# Not Found
