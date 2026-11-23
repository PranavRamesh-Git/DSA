class Node:
    def __init__(self,data = None,next=None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        self.head = None

    #insert at the beginning
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    #insert at the end
    def insert_at_end(self,data):
        node = Node(data)
        if not self.head:
            return self.insert_at_beginning(data)
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node
    #Insert at a specific index 
    def insert_at_index(self,data,index):
        node = Node(data)
        l = self.lengthll()  
        temp = self.head
        count = 0
        if index < 0 or index > l:
            print("INVALID INDEX")
            return
        if index == 0:
            return self.insert_at_beginning(data)
        elif index == l :
            return self.insert_at_end(data)
        else:
            while count + 1  != index :
                temp = temp.next
                count += 1
            node.next = temp.next
            temp.next = node
    #Insert after a given value/node
    def insert_after_value(self,data,value):
        node = Node(data)
        temp = self.head
        while temp:
            if temp.data == value:
                node.next = temp.next
                temp.next = node
                break
            else:
                temp = temp.next
        if temp is None :
            print("Value does not exist")


    #converting array into a linked list
    def array_ll(self,arr):
        self.head = None
        tail = None
        for data in arr:
            node = Node(data)
            if self.head is None:
                self.head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next

    #insert a node before a  node
    def insert_before_value(self,data,value):
        node = Node(data)
        if self.head is None:
            print("value does not exist")
            return 
        if value == self.head.data:
            return self.insert_at_beginning(data)
        temp = self.head
        prev = None

        while temp:
            if temp.data == value:
                break
            
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value does not exist")
        else:
            node.next = temp
            prev.next = node

    #Delete first node head
    def remove_head(self):
        if self.head is None:
            print("EMPTY")
            return
        self.head = self.head.next

    #delete tail or last node
    def remove_lastnode(self):
        if self.head is None:
            print("EMPTY")
            return            
        temp = self.head
        if temp.next is None:
            self.head = None
            return

        while  temp.next.next:
            temp = temp.next
        temp.next = None

    #Delete by index
    def delete_index(self,index):
        l = self.lengthll()
        if index > l - 1 or index < 0:
            print("INVALID INDEX")
            return
        elif index == 0: 
            return self.remove_head()
        elif index == l - 1:
            return self.remove_lastnode()
        else:
            temp = self.head
            count = 0
            while count + 1 != index :
                temp = temp.next
                count += 1
            temp.next = temp.next.next
    #delete by first occurrence value
    def delete_value(self,value):
        if self.head is None:
            print("EMPTY")
            return
        if self.head.data == value:
            return self.remove_head()
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                prev.next = temp.next
                break
            else:
                prev = temp
                temp = temp.next
    #delete by all occurrence value
    def delete_allvalues(self,value):
        if self.head is None:
            print("EMPTY")
            return
        while self.head and self.head.data == value:
            t = self.head.next
            self.head = t

        temp = self.head
        prev = Node(None)
        while temp:
            if temp.data == value:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

   

    #length of a linked list
    def lengthll(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    
    #display the linked list 
    def display(self):
        if self.lengthll() == 0:
            print("EMPTY!!!!")
        else:
            temp = self.head
            ll_str = ""

            while temp:
                ll_str += str(temp.data) + "->"
                temp = temp.next 
            ll_str += "None"
            print(ll_str)
    #search  value 
    def search_value(self,value):
        temp = self.head
        count = 0
        while temp and temp.data != value:
            temp = temp.next
            count += 1
        if not temp:
            print("value does not exist")
        else:
            print(f"Value exists on index {count}")

    #search index
    def search_index(self,index):
        temp = self.head
        l = self.lengthll()
        if index > l - 1 or index < 0 :
            print("INVALID INDEX")
            return
        else:
            if index == 0:
                print(self.head.data)
            else:
                count = 0
                while count != index:
                    temp = temp.next
                    count += 1
                print(temp.data)
    #Update value at an index
    def update_at_index(self,value,index):
        count = 0
        l = self.lengthll()
        temp = self.head
        if l - 1 < index or index < 0:
            print("Index doesnt exist") 
        else:
            while count != index:
                temp = temp.next
                count += 1
            temp.data = value
    
    #Clear the entire list
    def clear_list(self):
        if self.head is None:
            print("ALREADY EMPTY")
        else:
            self.head = None

    def reverse_ll(self):
        prev = None
        curr = self.head
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        self.head = prev

    def recursive_reverse_ll(self):
        def helper(curr,prev):
            if not curr:
                return prev
            curr_next = curr.next
            curr.next = prev
            return helper(curr_next,curr)
            
        self.head = helper(self.head,None)
        return self.head



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(4)
    print(ll.lengthll())
    ll.display()
    ll.insert_at_index(100,2)
    ll.display()
    ll.insert_at_index(200,1)
    ll.display()
    ll.insert_after_value(300,200)
    ll.display()    
    ll.insert_before_value(5,300)
    ll.display()
    ll.insert_before_value(1000,4)
    ll.display()
    ll.remove_head()
    ll.display()
    ll.remove_lastnode()
    ll.display()
    ll.delete_index(2)
    ll.display()
    ll.delete_index(3)
    ll.display() 
    ll.reverse_ll()
    ll.display()    
    ll2 = LinkedList()
    ll2.array_ll([2,2,3,2,4,2])
    ll2.display()
    ll2.delete_allvalues(2)
    ll2.display()                                     