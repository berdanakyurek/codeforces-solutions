def solve(s):
    count = 0
    for i in s.split():
        count += int(i)
    if count >= 2:
        return True
    return False

n = int(input())

res = 0
for i in range(n):
    if solve(input()):
        res += 1
print(res)
