N = int(input())

def is_bad(s):
    cnt = 0
    s = list(s)
    while len(s) > 0 and s[-1] == ")":
        s.pop()
        cnt += 1
    if cnt > len(s):
        return True
    return False

for i in range(N):
    input()
    s = input()
    if is_bad(s):
        print("Yes")
    else:
        print("No")