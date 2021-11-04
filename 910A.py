x = input().split()
n = int(x[0])
d = int(x[1])
arr = list(input())
frogLocation = 0
jumps = 0
while frogLocation != n - 1:
    x = frogLocation + d
    if x >= n:
        frogLocation = n
        jumps += 1
        break
    while x >= frogLocation:
        if x == frogLocation:
            jumps = -1
            break
        
        if arr[x] == '1':
            frogLocation = x
            jumps += 1
            break
        x -= 1
    if jumps == -1:
        break
print(jumps)