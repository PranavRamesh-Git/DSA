class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None

class circularll:
    def __init__(self):
        self.head = None
    
    def insert_beginning(self,data):
        temp = self.head
        node = Node(data)
        if temp is None:
            node.next = node
            self.head = node
            return

        while(temp.next != self.head):
            temp = temp.next
        
        tail = temp
        temp = self.head

        node.next = temp
        tail.next = node
        self.head = node

    def insert_end(self,data):
        temp = self.head
        if self.head is None:
            self.insert_beginning(data)
            return
        
        while (temp.next != self.head):
            temp = temp.next
        node = Node(data)
        node.next = self.head
        temp.next = node
        

