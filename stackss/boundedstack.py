class stack:
    def __init__(self,capacity):
        self.stack = []
        self.capacity = capacity
    
    def push(self,data):
        if(len(self.stack) == self.capacity):
            print("OVERFLOW")
            return
        self.stack.append(data)
    
    def pop(self):
        if(len(self.stack) == 0):
            return "EMPTY" 
        return self.stack.pop()       

    def peek(self):
        if(len(self.stack) == 0):
            return "EMPTY"         
        return self.stack[-1]
    def is_empty(self):
        if(len(self.stack) == 0):
            return "NOT EMPTY"
        return False

if __name__ == "__main__":
    s = stack(4)
    print(s.is_empty())
    s.push(10)
    s.push(20)
    print(s.peek())
    s.push(30)
    s.push(60)
    s.push(100)
    print(s.pop())
    s.push(20)
    print(s.pop())
    print(s.peek())        