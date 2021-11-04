def check(s):
    if s == "2020":
        return "YES"
    if s[:4] == "2020" or s[-4:] == "2020":
        return "YES"
    
    if s[:3] == "202" and s[-1] == '0':
        return "YES"
    
    if s[:2] == "20" and s[-2:] == "20":
        return "YES"
    if s[0] == "2" and s[-3:] == "020":
        return "YES"
    return "NO"

for i in range(int(input())):
    n = int(input())
    s = input()
    print(check(s))