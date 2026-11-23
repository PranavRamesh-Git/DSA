from collections import deque
def q_movingavg(stream,k):
    q = deque()
    ans = []
    count = 0
    avg = 0
    for i in stream:
        q.append(i)
        avg += i

        if len(q) > k:
            x = q.popleft()
            avg -= x
        
        ans.append(round(avg/len(q),2))
    return ans

class recentcounter:
    def __init__(self):
        self.q = deque()
        self.ans = []
    
    def ping(self,t):
        self.q.append(t)      
        while self.q and t - 3000 > self.q[0] :
            self.q.popleft()
        self.ans.append(len(self.q)) 
        print(len(self.q))
    
    def display(self):
        return self.ans

class rate_limiter:
    def __init__(self,limit,window):
        self.q = deque()
        self.ans = []
        self.limit = limit
        self.window = window
    
    def handle_requests(self,t):
        while self.q and  self.q[0] + self.window < t :
            x = self.q.popleft()

        if len(self.q) == 0 or len(self.q) < self.limit :
            self.q.append(t)
            self.ans.append('True')
        else:
            self.ans.append('False')
    
    def display(self):
        return self.ans



if __name__ == "__main__":
    k = 2
    stream = [4, 7, 2, 9]
    print(q_movingavg(stream,k))
    #------------------------------------------------------

    rc = recentcounter()
    rc.ping(1)     # 1
    rc.ping(100)   # 2
    rc.ping(3001)  # 3
    rc.ping(3002)  # 3
    print(rc.display())



