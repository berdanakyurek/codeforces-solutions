# Nov 4 2021

from math import log2

n = int(input())
arr = list(map(int, input().split()))

moves  = 0

for i in range(n - 1):

    if arr[i] != 0:
        arr[i + 2 ** int(log2(n-i-1))] += arr[i]
        moves += arr[i]
        arr[i] = 0
    print(moves)
