class circularqueue:
    def __init__(self,k):
        self.queue = [None]*k
        self.k = k
        self.size = 0
        self.front = 0
        self.rear = -1
    
    def enqueue(self,x):
        if(self.size == self.k):
            print("FULL")
            return
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = x
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            print("empty")
            return
        val = self.queue[self.front]

        self.queue[self.front] = None                    
        self.front = (self.front + 1) % self.k

        self.size -= 1
        print(val) 

if __name__ == "__main__":
    c = circularqueue(3)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.dequeue()
    c.dequeue()
    c.enqueue(4)
    c.dequeue()

        
