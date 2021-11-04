t = int(input())
for tt in range(t):
    a = input().split()
    x = int(a[0])
    y = int(a[1])
    k = int(a[2])
    print(((k + k * y-1) + (x - 1) - 1) // (x-1) + k)