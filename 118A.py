def solve(s):
    res = ''
    for l in s.lower():
        if not l in ['a', 'o', 'y', 'e', 'u', 'i']:
            res += "." + l
        
    return res

print(solve(input()))
