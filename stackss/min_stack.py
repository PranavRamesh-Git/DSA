class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        else:
            return "EMPTY"

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return "EMPTY"
    
    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

class Stackone:
    def __init__(self):
        self.stack = []
        self.min = 0
    
    def push(self,x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            diff = x - self.min
            self.stack.append(diff)
            if diff < 0:
                self.min = x
    
    def pop(self):
        if not self.stack:
            return "EMPTY"
        else:
            diff = self.stack.pop()
            if diff < 0:
                self.min =  self.min - diff
    
    def peek(self):
        if not self.stack:
            return "EMPTY"
        
        if self.stack[-1] < 0 :
            diff=  self.min
        else:
            diff = self.min +  diff 
        return diff
    
    def get_min(self):
        return self.min 
    






if __name__ == "__main__":
    s = Stack()
    s.push(2)
    print(s.min())
    s.push(5)
    s.push(1)
    print(s.min())
    print(s.top())
    s.pop()
    print(s.min())