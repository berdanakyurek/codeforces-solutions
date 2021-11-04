def foo(a,b):
    if a == b:
        return 0
    diff = (max(a,b) - min(a,b))
    if diff % 10 == 0:
        return int(diff / 10)
    return int( diff / 10) + 1

t = int(input())
for i in range(t):
    x = input().split()
    a = int(x[0])
    b = int(x[1])

    print(foo(a,b))

    
    