def check(s):
    ln = len(s)
    if s[0] == ')' or s[-1] == '(' or ln % 2 != 0:
        return "NO"
    
    countO = s.count('(')
    countC = s.count(')')
    countS = ln - countO - countC

    if min(countO, countC) + countS < max(countO, countC):
        return "NO"
    return "YES"


t = int(input())
for i in range(t):
    s = input()
    print(check(s))