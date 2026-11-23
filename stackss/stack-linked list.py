class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Ll:
    def __init__(self):
        self.stacktop = None

    def ll_len(self):
        temp = self.stacktop
        if temp is None:
            return 0
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
    def push(self,data):
        node = Node(data)
        if self.stacktop is None:
            node.next = None
            self.stacktop = node
            return
        node.next = self.stacktop
        self.stacktop = node
    
    def pop(self):
        if self.stacktop is None:
            return "UNDERFLOW"
        temp = self.stacktop.data
        self.stacktop = self.stacktop.next
        return temp
    
    def peek(self):
        if self.stacktop is None:
            return "EMPTY"
        return self.stacktop.data        
    
    def if_empty(self):
        if self.stacktop is None:
            return "EMPTY"
        return "NON EMPTY"