def solve(s):
    if len(s) <= 10:
        return s
    return s[0] + str(len(s) - 2) + s[-1]


n = int(input())

for i in range(n):
    print(solve(input()))
