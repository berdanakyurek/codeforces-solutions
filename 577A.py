def solve(n, x):
    if x == 1:
        return 1
    if x <=
    count = 0
    for i in range(n):
        for j in range(i, n):
            if (i+1) * (j+1) == x:
                count += 1
                if j != i:
                    count += 1
    return count

line = input().split()

n = int(line[0])
x = int(line[1])
print(solve(n, x))
