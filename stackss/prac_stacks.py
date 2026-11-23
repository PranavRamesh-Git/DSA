#PYTHON LIST / ARRAY IMPLEMENTATION
class stack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)


    def pop(self):
        if len(self.stack) == 0:
            print("STACK IS EMPTY")
            return

        self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def top(self):
        if not self.is_empty():
            print(stack[-1])
        else:
            print("EMPTY")

#LINKED LIST IMPLEMENTATION
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class LinkedList_stack:
    def __init__(self):
        self.top = None

    def push(self,x):
        node = Node(x)
        if self.top is None:
            self.top = node
            return

        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            print("EMPTY")
            return
        elif self.top.next is None:
            self.top = None
            return 
        new_top = self.top.next
        self.top.next = None
        self.top = new_top

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
    def top(self):
        if self.top is None:
            print("EMPTY")
            return

        print(self.top)

#Min stack with 2 stacks
class min_stack_two:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self,x):
        if not self.stack:
            self.stack.append(x)
            self.min.append(x)
            return
        self.stack.append(x)
        if x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        if not self.stack:
            print("EMPTY")
            return
        if self.stack[-1] > self.min[-1]:
            self.stack.pop()
        elif self.stack[-1] == self.min[-1]:
            self.stack.pop()
            self.min.pop()

    def min_element(self):
        if not self.stack:
            print("empty")
            return
        return self.min[-1]

    def top_element(self):
        if not self.stack:
            print("empty")
            return
        return self.stack[-1]

#MIN STACK WITH 1 STACK
class min_stack:
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self,x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
            return 
        if x > self.min:
            self.stack.append(x - self.min)
        else:
            self.stack.append(x - self.min)
            self.min = x

    def pop(self):
        if not self.stack:
            print("EMPTY")
            return 
        if self.stack[-1] < 0 :
            element = self.stack.pop()
            temp = self.min
            self.min = self.min - element
            return temp
        else:
            element = self.stack.pop()
            return self.min + element


    def peek(self):
        if not self.stack:
            print("EMPTY")
            return
        if self.stack[-1] >= 0:
            return self.min + self.stack[-1]
        else:
            return self.min
    def min_element(self):
        return self.min    

#BOUNDED STACK 
class bounded_stack:
    def __init__(self,capacity):
        self.stack = []
        self.capacity = capacity
        self.count = 0

    def push(self,x):
        if self.count + 1 > self.capacity:
            print("OVERFLOW")
            return
        self.stack.append(x)
        self.count += 1
    def pop(self):
        if self.count == 0:
            print("UNDERFLOW")
            return
        self.stack.pop()
        self.count -= 1

    def peek(self):
        if self.count == 0:
            print("EMPTY")
            return
        print(self.stack[-1])

    def current_capacity(self):
        print(self.count)

        
if __name__ == '__main__':
    s = bounded_stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.peek()
    s.current_capacity()


        
