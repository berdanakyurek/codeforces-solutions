def solve(s):
    hello = 'hello'
    hello_index = 0

    for l in s:
        if l == hello[hello_index]:
            hello_index += 1
        if hello_index >= 5:
            return "YES"
    return "NO"    

print(solve(input()))
