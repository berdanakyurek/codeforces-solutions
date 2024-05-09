import math

def solve(x, n):
    res = x // n
    if x % res == 0:
        return res
    sq = int(math.sqrt(x))
    if res > sq:
        res = sq
    while x % res != 0:
        res -= 1
    return res


n = int(input())

for i in range(n):
    s = input().split()
    print(solve(int(s[0]), int(s[1])))
