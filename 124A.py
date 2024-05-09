def solve(n, a, b):
    start = max(a, n - b - 1)
    return n - start

line = input().split()
n = int(line[0])
a = int(line[1])
b = int(line[2])

print(solve(n, a, b))
