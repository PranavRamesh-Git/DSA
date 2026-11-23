class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None    

class doublyll:
    def __init__(self):
        self.head = None
        self.tail = None
    #INSERTIONS
    def insert_at_beginning(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node


    def insert_at_end(self,data):
        node = Node(data)

        if self.head is None:
            self.insert_at_beginning(data)
            return

        temp = self.tail

        node.prev = temp
        temp.next = node
        self.tail = node


    def length_dll(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        return count

    def insert_at_index(self,index,data):
        node = Node(data)
        l = self.length_dll()
        if index > l   or index < 0 :
            print("Invalid Index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == l:
            self.insert_at_end(data)
            return

        count = 0
        temp = self.head
        while temp:
            if count + 1 == index:
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
                node.prev = temp
                return
            temp = temp.next
            count += 1

    def insert_before_node(self,value,data):
        if self.head is None:
            print("EMPTY list")
            return

        temp = self.head
        if self.head.data == value:
            self.insert_at_beginning(data)
            return
        node = Node(data)
        
        while temp:
            if temp.next and temp.next.data == value:
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
                node.prev = temp
                return
            temp = temp.next

        if temp is None:
            print("Node does not exist.")

    def insert_after_node(self,value,data):
        if self.head is None:
            print("EMPTY !!!")
            return

        temp = self.head
        node = Node(data)
        while temp:
            if temp.data == value:
                if temp.next is None:
                    self.insert_at_end(data)
                    return
                else:
                    node.next = temp.next
                    temp.next.prev = node
                    temp.next = node
                    node.prev = temp
                    return
            temp = temp.next

        if temp is None:
            print("Node does not exist")

    #DELETIONS
    def delete_first_node(self):
        if self.head is None:
            print("EMPTY!!!")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return

        temp = self.head.next
        temp.prev = None
        self.head.next = None
        self.head = temp

    def delete_last_node(self):
        if self.head is None:
            print("EMPTY !!")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        node = temp.prev
        temp.prev = None
        node.next = None
        temp.next = None
        self.tail = node

    def delete_value(self,value):
        if self.head is None:
            print("EMPTY")
            return
        if self.head.data == value:
            self.delete_first_node()
            return
        elif self.tail.data == value:
            self.delete_last_node()
            return

        temp = self.head
        while temp:
            if temp.next and temp.next.data == value:
                node = temp.next.next
                temp.next.next = None
                temp.next.prev = None
                temp.next = node
                node.prev = temp
                return
            temp = temp.next

        if temp is None:
            print("Node with given value does not exist")

    def delete_at_index(self,index):
        count = 0
        l = self.length_dll()

        if index > l - 1 or index < 0 :
            print("INVALID INDEX")
            return

        if index == 0:
            self.delete_first_node()
            return
        elif index == l - 1:
            self.delete_last_node()
            return

        temp = self.head
        while temp:
            if count + 1 == index:
                node = temp.next.next
                temp.next.next = None
                temp.next.prev = None
                temp.next = node
                node.prev = temp
                return
            temp = temp.next
            count += 1




    def display_list_front(self):
        if self.head is None:
            print("LIST IS EMPTY !!!")
            return

        temp = self.head
        ans = ""
        while temp:
            ans += f"{temp.data}->" 
            temp = temp.next
        ans += "None"
        print(ans)

    def length_dll(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def display_list_back(self):
        if self.head is None:
            print("EMPTY !!!")
            return

        temp = self.tail
        #print("self.tail is: ",self.tail.data)
        #print("self.head is: ",self.head.data)
        ans = ""
        while temp:
            ans += f"{temp.data}<-" 
            temp = temp.prev

        ans += "None"
        print(ans)

    def search_value(self,value):
        if self.head is None:
            print("EMPTY!!!!")
            return
        temp = self.head
        count = 0
        while temp:
            if temp.data == value:
                print(f"Node with {value} is at index {count}")
                return
            count += 1
            temp = temp.next

        if temp is None:
            print(f"No node with value {value} exists ")

    def reverse_dll(self):
        curr = self.head
        dummy = curr
        temp = None
        while curr:
            curr_next = curr.next
            curr.prev = curr_next
            curr.next =  temp
            temp = curr
            curr = curr_next
        self.head = temp
        self.tail = dummy
    def delete_duplicates_unsorted(self):
        s = set()
        if self.head is None:
            print("EMPTY!!!!")
            return
        temp = self.head

        s.add(self.head.data)
        while temp and temp.next:
            if temp.next.data not in s:
                s.add(temp.next.data)
                temp = temp.next
            else:
                duplicate = temp.next

                if duplicate.next is None:
                    temp.next = None
                    duplicate.prev = None
                    self.tail = temp
                else:
                    node = duplicate.next

                    temp.next.next = None
                    temp.next.prev = None
                    temp.next = node
                    node.prev = temp

    def delete_duplicates_sorted(self):
        if self.head is None:
            print("EMPTY")
            return

        temp = self.head

        while temp and temp.next:
            if temp.next.data == temp.data:
                if temp.next.next is None:
                    temp.next.prev = None
                    temp.next = None
                    self.tail = temp
                else:
                    node = temp.next.next
                    temp.next.prev = None
                    temp.next.next = None
                    temp.next = node
                    node.prev = temp
            else:
                temp = temp.next



if __name__ == '__main__':
    dll = doublyll()
    dll.insert_at_beginning(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(4)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.insert_at_end(5)    
    dll.display_list_front()
    dll.delete_duplicates_sorted()
    dll.display_list_front()
    dll.display_list_back()