def foo(n, k, d, total, dSatisfied, cache):
    toStr = "%d %d %d %d %d" % (n,k,d,total,int(dSatisfied))
    #print(toStr)

    if toStr in cache:
        return cache[toStr]

    if total == n:
        if dSatisfied == True:
            return 1
        return 0

    toRet = 0
    for i in range(1, k+1):
        if total + i > n:
            break
        dst = dSatisfied
        if i >= d:
            dst = True
        recResult = foo(n, k, d, total + i, dst, cache)

        if recResult != -1:
            toRet += recResult

    cache[toStr] = toRet
    return toRet

inp = input().split()
n = int(inp[0])
k = int(inp[1])
d = int(inp[2])
print(foo(n, k, d, 0, False, {}) % 1000000007)
