def solve(n, t):
    res = ""
    if n == 1:
        if t == 10:
            return -1
        return t
    if t <= 9:
        for i in range(n):
            res += str(t)
    if t == 10:
        return t ** (n-1)
    return res
    
line = input().split()
n = int(line[0])
t = int(line[1])

print(solve(n, t))
