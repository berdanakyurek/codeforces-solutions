inp = input().split()
n = int(inp[0])
k = int(inp[1])
d = int(inp[2])

# cache[n][0]: result of all with n
# cache[n][1]: result of containing at least one >= d
cache = []
cache.append([1,0])

for i in range(1, n+1):
    count = 0
    count2 = 0

    for j in range(1, min(k+1, i+1)):
        count += cache[i-j][0]

    for j in range(1, min(k+1, i+1)):
        if j < d:
            count2 += cache[i-j][1]
        else:
            count2 += cache[i-j][0]
    cache.append([count, count2])

print(cache[n][1] % 1000000007)
