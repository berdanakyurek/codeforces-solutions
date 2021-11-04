def foo(n):
    if n == 1:
        return 1
    return foo(n-1) + 4 * n - 4
print(foo(int(input())))
