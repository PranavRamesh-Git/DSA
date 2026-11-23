def next_greater_element(s):
    stack = []
    res = [-1]*len(s)

    for i in range(len(s)):
        while stack and s[stack[-1]] < s[i]:
            idx = stack.pop()
            res[idx] = s[i]
        stack.append(i)
    
    return res
def next_lesser_element(s):
    stack = []
    res = [-1]*len(s)

    for i in range(len(s)):
        while stack and s[stack[-1]] > s[i]:
            idx = stack.pop()
            res[idx] = s[i]
        stack.append(i)

    return res

def previous_greater_element(s):
    stack = []
    res = [-1]*len(s)
    for i in range(len(s)):
        while stack and s[stack[-1]] <= s[i]:
            idx = stack.pop()
        if  stack:
            res[i] = s[-1]
        stack.append()
    return res

def previous_lesser_element(s):
    return 0



if __name__ == "__main__":
    s = [2, 1, 2, 4, 3]
    #print(next_greater_element(s))
    t = [4, 5, 2, 10, 8]
    #print(next_lesser_element(t))

    print(previous_greater_element(s))