#Created a Linked List with a list of items with insert at particular Index 
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
        self.length+=1
        
    def appendListAtIndex(self, data, index):
        if index < 0 or index >= self.length:
            print(f'Please enter a number>=0 and number<={self.length}')
            return
        
        new_data = Node(data)
        if index == 0:
            new_data.next = self.head
            self.head = new_data
        else:
            count = 0
            current = self.head
            while count < index:
                current = current.next
                count+=1 
            new_data.next = current.next
            current.next = new_data
        self.length +=1 
        return self.displayList(data, index)
                
    def iterateListItems(self, listdata):
        for data,index in listdata:
            self.appendListAtIndex(data, index)

    def displayList(self, data = None, index = None):
        current = self.head
        s = ''
        while current:
            s+= str(current.data) + ' --> '
            current = current.next
        s+='null'
        print(s if data is None else f'Inserted {data} at Index no {index}:\n{s}')
        
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.displayList()
ll.iterateListItems([(100,1), (200,1), (-300,5), (91,0), (45, 8)])

# Output
# 10 --> 20 --> 30 --> 40 --> null
# Inserted 100 at Index no 1:
# 10 --> 20 --> 100 --> 30 --> 40 --> null
# Inserted 200 at Index no 1:
# 10 --> 20 --> 200 --> 100 --> 30 --> 40 --> null
# Inserted -300 at Index no 5:
# 10 --> 20 --> 200 --> 100 --> 30 --> 40 --> -300 --> null
# Inserted 91 at Index no 0:
# 91 --> 10 --> 20 --> 200 --> 100 --> 30 --> 40 --> -300 --> null
# Please enter a number>=0 and number<=8
