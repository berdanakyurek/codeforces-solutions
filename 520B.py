called = {}
def solve(n, m):
    print(n,m)
    if "%d,%d"%(n,m) in called:
        return called["%d,%d"%(n,m)]
    called["%d,%d"%(n,m)] = 9999999999
    if m == n:
        called["%d,%d"%(n,m)] = 0
        return 0
    if 2*n == m:
        called["%d,%d"%(n,m)] = 1
        return 1
    if n > m:
        called["%d,%d"%(n,m)] = n - m
        return n-m
    if 2*n < m:
        result = solve(2*n, m) + 1
        called["%d,%d"%(n,m)] = result
        return result

    # if n > m/2:
    #     if m % 2 == 0:
    #         return min(n-m/2+1, 2*n - m + 1)
    #     else :
    #         return min(n-(m//2+1)+2, 2 * n - m + 1)

    #result =  min(solve(2*n, m) + 1, n-m/) + 1
    result = 99999999999
    if m % 2 == 0:
        result = n - m // 2 + 1
        print("here", n, m)
        print(result)
    else:
        result = n - (m // 2 + 1) + 2

    result = min(1 + solve(2*n, m), result)
    called["%d,%d"%(n,m)] = result
    return result



nm = input().split()
n = int(nm[0])
m = int(nm[1])

print(solve(n,m))
