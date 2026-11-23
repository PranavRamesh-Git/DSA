class stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return "EMPTY"
        return "NOT EMPTY"
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty() == "EMPTY":
            return "UNDERFLOW"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty() == "EMPTY":
            return "STACK IS EMPTY "
        return self.stack[-1]
    
if __name__ == "__main__":
    s = stack()
    print(s.is_empty())
    s.push(10)
    s.push(20)
    print(s.peek())
    s.push(30)
    print(s.pop())
    s.push(60)
    print(s.pop())
    print(s.peek())