def solve(n):
    if n == 1:
        return 1
    
    if(n % 2 == 0):
        return solve(n // 2)
    return 1 + solve((n-1) // 2)

print(solve(int(input())))

