#using deque
from collections import deque
class queue_deque:
    def __init__(self):
        self.q = deque()

    def push(self,x):
        self.q.append(x)

    def pop(self):
        if self.empty():
            print("EMPTY")
            return
        x = self.q.popleft()
        print("element popped :",x)

    def peek(self):
        if self.empty():
            print("EMPTY")
            return
        print("top element :",self.q[0])

    def empty(self):
        if(len(self.q) == 0):
            return True
        return False

#using list
class queue_list:
    def __init__(self):
        self.q = []


    def push(self,x):
        self.q.append(x)

    def pop(self):
        if self.empty():
            print("EMPTY")
            return
        x = self.q.pop(0)
        print("popped element :",x)

    def peek(self):
        if self.empty():
            print("EMPTY")
            return
        print("top element :",self.q[0])

    def empty(self):
        if(len(self.q) == 0):
            return True
        return False

#using queue
from queue import Queue
class queue_Queue:
    def __init__(self):
        self.q = Queue()


    def push(self,x):
        self.q.put(x)

    def pop(self):
        if self.empty():
            print("EMPTY")
            return
        x = self.q.get()
        print("element popped :",x)

    def peek(self):
        if self.empty():
            print("EMPTY")
            return
        with self.q.mutex:
            print("top element :",self.q.queue[0])

    def empty(self):
        if(self.q.empty()):
            return True
        return False
    
#using queue of fixed length
class queue_fixedQueueSize:
    def __init__(self):
        self.q = Queue(5)


    def push(self,x):
        if(self.q.full()):
            print("FULL")
            return
        self.q.put(x)

    def pop(self):
        if self.empty():
            print("EMPTY")
            return
        x = self.q.get()
        print("element popped :",x)


    def peek(self):
        if self.empty():
            print("EMPTY")
            return
        with self.q.mutex:
            print("front element :", self.q.queue[0])


    def empty(self):
        if(self.q.empty()):
            return True
        return False      
#queue with 2 stacks

class queue_from2stacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self,x):
        self.s1.append(x)

    def pop(self):
        if not self.s1:
            print("EMPTY")
            return
        while self.s1:
            self.s2.append(self.s1.pop())

        x =  self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
    def peek(self):
        if not self.s1:
            print("EMPTY")
            return
        return self.s1[0]
    def is_empty(self):
        return (len(self.s1) == 0)

#stack from 2 queues
from collections import deque

class stack_from2queues:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x):
        self.s2.append(x)

        while self.s1:
            self.s2.append(self.s1.popleft())

        self.s1, self.s2 = self.s2, self.s1

    def pop(self):
        if len(self.s1) == 0:
            return "EMPTY"

        return self.s1.popleft()

    def top(self):
        if len(self.s1) == 0:
            return "EMPTY"

        return self.s1[0]

    def empty(self):
        return len(self.s1) == 0


if __name__ == '__main__':
    s = stack_from2queues()
    s.push(10)
    s.push(20)
    s.push(30)
    
    print(s.top())
    print(s.pop())
    print(s.top())
    s.push(40)
    print(s.top())










"""
What is mutex?
Mutex = Mutual Exclusion

Suppose two threads are accessing the same queue:
- Thread 1 wants to read the front element.
- Thread 2 wants to remove the front element.
If both access the queue simultaneously, unexpected behavior can occur.

A mutex ensures that only one thread at a time can access the protected data.

the with self.q.mutex: do?
It automatically acquires and releases the lock.

with self.q.mutex:
    print(self.q.queue[0]) 


is equivalent to 


self.q.mutex.acquire()  # Lock

try:
    print(self.q.queue[0])
finally:
    self.q.mutex.release()  # Unlock

"""