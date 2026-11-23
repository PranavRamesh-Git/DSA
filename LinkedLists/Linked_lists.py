class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    
class Linkedlists:
    def __init__(self):
        self.head = None
    
    def insertatbeginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insertatend(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def lengthll(self):
        count = 0
        if self.head is None:
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    #create a new linked list with set of values from the given array/list
    def create_ll(self,arr):
        self.head = None
        for data in arr:
            node = Node(data,None)            
            if(self.head is None):
                self.head = node
                continue
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
     
    def insertatindex(self,data,index):
        if index < 0 or index > self.lengthll():
            print("Invalid Index")
            return
        
        if index == 0:
            node = Node(data,self.head)
            self.head = node
            return 
        
        if index == self.lengthll():
            node = Node(data,None)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            return

        temp = self.head
        count = 0
        while temp:
            if(count == index -1):
                node = Node(data,temp.next)
                temp.next = node
                return
            count += 1
            temp = temp.next

    def removeatindex(self,index):

        if(self.head is None):
            print("EMPTY !!!")
            return 
        
        if index < 0 or index >= self.lengthll():
            print("Invalid Index")
            return


        if(index == 0):
            self.head = self.head.next
            return
        
        count = 0
        temp = self.head
        while temp:
            if(count == index - 1):
                temp.next = temp.next.next
                return
            count += 1
            temp = temp.next
    
    def printll(self):
        llstr = ""
        if self.head is None:
            print("LINKED LIST IS EMPTY !!!!")
            return
        temp = self.head
        while temp:
            llstr += str(temp.data) + "->"
            temp = temp.next
        llstr += "None"
        print(llstr)
    
    def reverse_ll(self):
        prev = None
        curr = self.head
        while curr != None:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        self.head = prev

if __name__ == "__main__":
    l = Linkedlists()
    l.insertatbeginning(20)
    l.insertatbeginning(10)
    l.insertatbeginning(5)
    l.insertatend(30)
    l.insertatend(50)
    l.insertatbeginning(1)
    l.printll()
    print(l.lengthll())
    l2 = Linkedlists()
    l2.create_ll([10,20,30,50,100,200,500])
    l2.insertatbeginning(5)
    l2.insertatend(600)
    l2.printll()
    print(l2.lengthll())
    l2.insertatindex(25,3)
    l2.printll()
    l2.removeatindex(0)
    l2.printll()
    print(l2.lengthll())
    l2.removeatindex(8)
    l2.printll()