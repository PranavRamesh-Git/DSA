from collections import deque
from queue import Queue,Full,Empty

class queue_list:
    def __init__(self):
        self.queue = []

    def empty(self):
        if(len(self.queue) == 0):
            return True
        return False

    def put(self,x):
        self.queue.append(x)

    def get(self):
        if self.empty():
            return "EMPTY"
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    
class q_deque:
    def __init__(self):
        self.queue = deque()

    def empty(self):
        if(len(self.queue) == 0):
            return True
        return False

    def put(self,x):
        self.queue.append(x)

    def get(self):
        if self.empty():
            return "EMPTY"
        return self.queue.popleft()
    def size(self):
        return len(self.queue) 

class q_queue:
    def __init__(self):
        self.queue = Queue(5)

    def put_element(self,x):
        self.queue.put(x)

    def get_element(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize()

class q1_queue:
    def __init__(self):
        self.queue = Queue(5)

    def put_element(self,x):
        self.queue.put(x)

    def get_element(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize()

    def put_nowait(self,x):
        try: 
            self.queue.put_nowait(x)
        except Full:
            print("Queue is Full")
        
    
    def get_nowait(self):
        try:
            return self.queue.get_nowait()
        except Empty:
            print("Queue is empty")



                
    

if __name__ == "__main__":
    q = queue_list()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(q.size())
    print(q.get())
    print(q.get())
    print(q.empty())
    print("---------------------------------------------")
    q1 = q_deque()
    q1.put(1)
    q1.put(2)
    q1.put(3)
    q1.put(4)
    print(q1.size())
    print(q1.get())
    print(q1.get())
    print(q1.empty())


