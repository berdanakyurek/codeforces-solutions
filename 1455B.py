def foo(x):
    curr = 0
    k = 1
    while True:

        if curr == x:
            return k-1
        if curr > x:
            if curr - 1 == x:
                k += 1
            return k-1
        curr += k
        k += 1

t = int(input())
for i in range(t):
    print(foo(int(input())))