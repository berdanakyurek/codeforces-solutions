# Nov 4 2021

inp = input().split()

n = int(inp[0])
l = int(inp[1])

arr = list(map(int, input().split()))

arr.sort()

d = max(arr[0], l - arr[-1])

for i in range(1, n):
    minV = (arr[i] - arr[i - 1]) / 2

    if minV > d:
        d = minV

print(d)
