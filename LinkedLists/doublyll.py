class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class doublelinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = node
            return
        node.next = temp
        temp.prev = node
        self.head = node
    
    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = node
        node.prev = temp

    def length(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count


    def insert_at_index(self,index,data):
        if self.head is None:
            print("EMPTY")
            return 
        
        ll = self.length()

        if(index < 0 or index > ll):
            print("INVALID INDEX")
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        temp = self.head
        while (count < index - 1):
            temp = temp.next
            count += 1
        
        node = Node(data)

        node.next = temp.next
        node.prev = temp

        if temp.next is not None:
            temp.next.prev = node

        temp.next = node
        
    def delete_by_value(self,value):
        temp = self.head

        while temp and (temp.data != value):
            temp = temp.next

        if(temp is None):
            return

        if(temp == self.head):
            self.head = temp.next
            if temp.next:
                self.head.prev = None
                return
    
        temp.prev.next = temp.next
        if(temp.next):
            temp.next.prev = temp.prev
    
    def reversal_dll(self):
        curr = self.head
        temp = None
        if curr is None:
            return
        while curr:
            nxt = curr.next
            prevv = curr.prev
            curr.next = prevv
            curr.prev = nxt
            temp = curr
            curr = nxt
        if temp is not None:
            self.head = temp




        
