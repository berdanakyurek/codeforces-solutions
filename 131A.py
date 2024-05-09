def solve(s):
    res = ""
    for i in range(len(s)):
        if(s[i].isupper()):
            res += s[i].lower()
        else:
            if i > 0:
                return s
            res += s[i].upper()
    return res

print(solve(input()))
