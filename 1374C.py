def solve(s):
    moves = 0
    stack = []

    i = 0
    while i < len(s):
        element = s[i]
        if element == "(":
            stack.append(element)
        elif len(stack) == 0:
            moves += 1
            s.append(s.pop(i))
            i -= 1
        else:
            stack.pop()
        i += 1
    stack = []
    i = len(s) - 1
    while i >= 0:
        element = s[i]
        if element == ")":
            stack.append(element)
        elif len(stack) == 0:
            moves += 1
            s.insert(0, s.pop(i))
            i += 1
        else:
            stack.pop()
        i -= 1
    return moves

t = int(input())
for i in range(t):
    input()
    print(solve([*input()]))
