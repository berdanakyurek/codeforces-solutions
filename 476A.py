def solve(n, m):
    if n < m:
        return -1
    if n == m:
        return n
    minimum = n // 2
    if n % 2 == 1:
        minimum += 1
    if minimum % m == 0:
        return minimum

    return (minimum // m + 1) * m

split = input().split()

print(solve(int(split[0]), int(split[1])))
