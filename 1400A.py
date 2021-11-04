t = int(input())
for i in range(t):
    n = int(input())
    st = input()
    w = ""
    for i in range(0,n):
        subst = st[i: n+i]
        # print(subst)
        w += subst[i]

    print(w)