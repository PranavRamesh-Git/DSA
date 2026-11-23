def infix_postfix(s):
    output = []
    stack = []

    precedence = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    for ch in s:

        if ch == " ":
            continue

        elif ch.isalnum():
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':

            while stack and stack[-1] != '(':
                output.append(stack.pop())

            stack.pop()

        else:

            while (
                stack
                and stack[-1] != '('
                and (
                    precedence[stack[-1]] > precedence[ch]
                    or (
                        precedence[stack[-1]] == precedence[ch]
                        and ch != '^'
                    )
                )
            ):
                output.append(stack.pop())

            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return "".join(output)


def postfix_to_prefix(s):
    stack = []

    for ch in s:

        if ch.isalnum():
            stack.append(ch)

        else:
            right = stack.pop()
            left = stack.pop()

            stack.append(ch + left + right)

    return stack[-1]


def prefix_to_postfix(s):
    stack = []

    for ch in reversed(s):

        if ch.isalnum():
            stack.append(ch)

        else:
            left = stack.pop()
            right = stack.pop()

            stack.append(left + right + ch)

    return stack[-1]


def postfix_eval(s):
    stack = []

    for ch in s:

        if ch.isdigit():
            stack.append(int(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a / b)

    return stack[-1]


def prefix_eval(s):
    stack = []

    for ch in reversed(s):

        if ch.isdigit():
            stack.append(int(ch))

        else:
            a = stack.pop()
            b = stack.pop()

            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a / b)

    return stack[-1]