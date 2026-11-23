def reversee(s):
    stack = []
    ans = ""
    for i in s:
        stack.append(i)
    ans = []
    while len(stack) > 0:
        ans.append(stack.pop())
    return "".join(ans)

def remove_adjacentdup(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)

def backspace(s):
    stack = []
    for i in s:
        if stack and i == '#':
            stack.pop()
        elif len(stack) == 0 and i == '#':
            continue
        else:
            stack.append(i)
    return "".join(stack)

def valid_parenthesis(s):
    stack = []
    #"()[]{}", (([]))
    mapping = {')' : '(' , '}' : '{' , ']' : '['}
    for i in s:
        if i in mapping:
            if not stack or stack[-1] != mapping[i]:
                return False
            if stack:
                stack.pop()
        else:
            stack.append(i)

    if(len(stack) == 0):
        return True
    return False



def postflix(s):
    stack = []
    for i in s:
        if i.isdigit():
            stack.append(int(i))
        else:
            b = stack.pop()
            a  = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)
    return stack[-1]      


def prefix(s):
    stack = []
    for i in s[::-1]:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b  = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)
    return stack[-1]      

def infix_postfix_convert(s):
    stack = []
    output = []
    d = {'+': 1,'-': 1,'*': 2,'/': 2}
    for i in s:
        if i.isalnum():
            output.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and d[stack[-1]] >= d[i]:
                output.append(stack.pop())
            stack.append(i)
    while stack:
        output.append(stack.pop())    
            

    return "".join(output)
def infix_prefix_convert(s):
    s = s[::-1]
    t = []
    for i in s:
        if i == '(':
            t.append(')')
        elif i == ')':
            t.append('(')
        else:
            t.append(i)
    postfix = infix_postfix_convert("".join(t))
    return postfix[::-1]



if __name__ == "__main__":
    s = "My name is Pranav"
    print(infix_postfix_convert("A+B*C"))
    print(infix_postfix_convert("(A+B)*C"))     # AB+C*
    print(infix_postfix_convert("A*(B+C/D)"))   # ABCD/+*
    print(infix_postfix_convert("A-B+C"))       # AB-C+
    print(infix_postfix_convert("((A+B)*C)"))   # AB+C*

    print(infix_prefix_convert("A+B*C"))        # +A*BC
    print(infix_prefix_convert("(A+B)*C"))      # *+ABC
    print(infix_prefix_convert("A*(B+C/D)"))    # *A+B/CD