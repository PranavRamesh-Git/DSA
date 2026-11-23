class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_ll:
    def __init__(self):
        self.head = None
    

    def insert_at_beginning(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next  = self.head
            self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head  = node
            node.next = self.head
        else:

            temp = self.head
            while temp.next != self.head :
                temp = temp.next

            
            temp.next = node
            node.next = self.head
    def insert_at_index(self,index,data):
        node = Node(data)
        if self.head is None and index > 0 :
            print("EMPTY!!!")
            return
        l = self.length_ll()
        if index == 0 or (not l and index == 0):
            self.insert_at_beginning(data)
            return
        elif index == l:
            self.insert_at_end(data)
            return
        elif index < 0 or index > l:
            print("INVALID INDEX")
            return
        else:
            count = 0
            temp = self.head
            while temp.next != self.head:
                if count + 1 == index:
                    temp_next = temp.next
                    temp.next = node
                    node.next = temp_next 
                    return
                count += 1
                temp = temp.next

    def delete_from_beginning(self):
        if self.head is None:
            print("EMPTY LIST")
            return
        temp = self.head
        if temp.next == self.head:
            self.head = None
            print("EMPTY")
            return
        temp = self.head
        new_head = temp.next

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_head
        self.head = new_head

    def delete_from_end(self):
        if self.head is None:
            print("EMPTY!!")
            return
        temp = self.head
        if temp.next == self.head:
            self.head = None
            print("EMPTY")
            return
        temp = self.head
        while temp.next and temp.next.next != self.head :
            temp = temp.next

        temp.next = self.head

    def delete_at_index(self,index):
        if self.head is None:
            print("EMPTY!!")
            return

        count = 0
        l = self.length_ll()
        if index == 0:
            self.delete_from_beginning()
            return
        if index == l -1:
            self.delete_from_end()
            return
        if index < 0 or index >= l:
            print("INVALID INDEX")
            return

        temp = self.head
        while temp.next != self.head:
            if count + 1 == index:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1

                          
    def display_list(self):
        if self.head is None:
            print("EMPTY!!!")
            return
        c = ""
        temp = self.head
        while temp.next != self.head:
            c += str(temp.data) + "->"
            temp = temp.next
        c += str(temp.data) + "->" + str(temp.next.data)
        print(c)

    def reverse_circular_list(self):
        if self.head is None:
            print("EMPTY LIST !!!")
            return
        temp = self.head
        if temp.next == self.head:
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = None
        curr = self.head
        temp = self.head
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        self.head = prev
        temp.next = prev

    def search_value(self,value):
        if self.head is None:
            print("EMPTY!! DOES NOT EXIST")
            return
        temp = self.head
        count = 0
        if temp.data == value:
            print(f"{value} is at index-> {count}")
            return
        count += 1
        temp = temp.next
        while temp != self.head:
            if temp.data == value:
                print(f"{value} is at index-> {count}")
                return
            count += 1
            temp = temp.next
        
        if temp == self.head:
            print(f"{value} does not exist")
        

        
    def length_ll(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def check_circular(self):
        if self.head is None:
            return False
        temp = self.head
        while temp.next and temp.next != self.head:
            temp = temp.next

        if temp.next == self.head:
            return True
        return False

    
if __name__ =='__main__':
    c = circular_ll()
    c.insert_at_beginning(10)
    c.insert_at_end(20)
    c.insert_at_end(30)
    c.insert_at_end(40)
    c.display_list()
    print(c.length_ll())
    c.insert_at_index(2,100)
    c.display_list()
    c.insert_at_index(3,200)
    c.display_list()
    c.search_value(30)
    c.delete_at_index(4)
    c.display_list()
    c.reverse_circular_list()
    c.display_list()
    print(c.check_circular())
