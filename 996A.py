def foo(n):
    total = 0
    moneys = [100,20,10,5,1]
    for x in moneys:
        a = n // x
        total += a
        n -= a*x
    return total

print(foo(int(input())))