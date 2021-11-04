import math

def compute_total(n, k):
    if k >= n:
        return k
    if n % k == 0:
        return n
    return n + (k - (n % k))

def foo(n,k):
    total = compute_total(n, k)
    return math.ceil(total/n)        

t = int(input())
for i in range(t):
    x = input().split()
    n = int(x[0])
    k = int(x[1])
    print(foo(n, k))