from collections import deque
from queue import Queue,Full,Empty
#queue using list 
class q_list:
    def __init__(self):
        self.q = []
    
    def enqueue(self,x):
        self.q.append(x)
    
    def dequeue(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        else:
            return "Empty"
        
    
    def peek(self):
        if len(self.q) == 0:
            return "EMPTY"
        else:
            return self.q[0]
        
    def display(self):
        l = len(self.q)
        for i in range(l):
            if i == l - 1:
                print(self.q[i])
            else:
                print(self.q[i],end = "<-")

#queue using deque
class q_deq:
    def __init__(self):
        self.q = deque()
    
    def enqueue(self,x):
        self.q.append(x)
    
    def dequeue(self):
        if len(self.q) > 0:
            return self.q.popleft()
        else:
            return "Empty"
        
    
    def peek(self):
        if len(self.q) == 0:
            return "EMPTY"
        else:
            return self.q[0]
        
    def display(self):
        l = len(self.q)
        for i in range(l):
            if i == l - 1:
                print(self.q[i])
            else:
                print(self.q[i],end = "<-")
#queue using Queue
class q_Queue:
    def __init__(self):
        self.q = Queue(5)
    
    def enqueue(self,x):
        try:
            self.q.put_nowait(x)
        except Full:
            print("Queue is full")
    
    def dequeue(self):
        try:
            return self.q.get_nowait()
        except Empty:
            return("EMPTY")
        
    
    def peek(self):
        if self.q.empty():
            return "EMPTY"
        else:
            return self.q.queue[0]
        
    def display(self):
        if self.q.empty():
            print('EMPTY')
        else:
            print("<-".join(map(str,list(self.q.queue)))) # map()-> converts number to strings - [1,2,3] -> ["1","2","3"]

#queue using 2 stacks
class q_stacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    
    def dequeue(self):
        if len(self.s1) > 0:
            return self.s1.pop()
        else:
            return "Empty"
        
    
    def peek(self):
        if len(self.s1) == 0:
            return "EMPTY"
        else:
            return self.s1[-1]
        
    def display(self):
        l = len(self.s1)
        for i in range(l-1,-1,-1):
            if i == 0:
                print(self.s1[i])
            else:
                print(self.s1[i],end = "->")
#stack using 2 queue
class q_stackq:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def enqueue(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1
    
    def dequeue(self):
        if self.q1:
            return self.q1.popleft()
        else:
            return "EMPTY"
    def peek(self):
        if self.q1:
            return self.q1[0]
        else:
            return "EMPTY"

    def display(self):
        l = len(self.q1)
        for i in range(l):
            if i == l - 1:
                print(self.q1[i])
            else:
                print(self.q1[i],end = "->")               
        

#circular queue
class q_cir:
    def __init__(self,k):
        self.q = [None] * k
        self.k = k
        self.front = -1
        self.rear = -1
    def isempty(self):
        if self.front == -1:
            return True
        else:
            return False
        
    def isfull(self):
        if (self.rear + 1) % self.k == self.front:
            return True
        else:
            return False        

    def enqueue(self,x):
        if self.isfull():
            return "FULL"
        
        if self.isempty():
            self.front = 0

        self.rear = (self.rear + 1) % self.k

        self.q[self.rear] = x
    
    def dequeue(self):
        if self.isempty():
            return "EMPTY"
        
        x = self.q[self.front]
        self.q[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.k
        
        return x

    def peek(self):
        if self.front == -1:
            return "EMPTY"
        else:
            return self.q[self.front]
    
    def display(self):
        for i in range(self.k):                
            print(f"Index {i}",end = "->")
        print("Index 0")
        for i in range(self.k):
            print(self.q[i],end = "->")
        print(self.q[0])



#queue using circular dequeu
class q_circdequeue:
    def __init__(self,k):
        self.q = [None]* k
        self.k = k
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        if self.front == -1:
            return True
        return False
    
    def is_full(self):
        if (self.rear + 1) % self.k == self.front:
            return True
        return False
    
    def add_front(self,x):
      
        if self.is_full():
            print("QUEUE IS FULL")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.front = (self.front - 1 + self.k) % self.k 
            self.q[self.front] = x
    
    def add_rear(self,x):     
        if self.is_full():
            print("QUEUE IS FULL")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:  
                self.rear = (self.rear + 1) % self.k
            self.q[self.rear] = x
    
    def rem_front(self):
        if self.is_empty():
            return "EMPTY"
        
        x = self.q[self.front]
        self.q[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.k
        return x
    
    def rem_back(self):
        if self.is_empty():
            return "EMPTY"
        
        x = self.q[self.rear]
        self.q[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.k) % self.k
        return x
    
    def display(self):
        for i in range(self.k):                
            print(f"Index {i}",end = "->")
        print("Index 0")
        for i in range(self.k):
            print(self.q[i],end = "->")
        print(self.q[0])        
            
#queue using linked lists



if __name__ == "__main__":
    q1 = q_cir(5)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.display()
    print(q1.peek())
    print(q1.dequeue())
    q1.display()
    q1.dequeue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.display()
