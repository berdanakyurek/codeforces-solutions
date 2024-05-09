def solve(n):
    if n == 0:
        return 1
    remainder = n % 4

    if remainder == 0:
        return 6
    if remainder == 3:
        return 2
    if remainder == 2:
        return 4
    if remainder == 1:
        return 8
    return 0

print(solve(int(input())))
