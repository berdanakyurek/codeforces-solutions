t = int(input())
for i in range(t):
    n = int(input())
    a1 = input().split()
    a2 = input().split()
    a3 = input().split()
    w = []
    for j in range(n):
        if len(w) == 0:
            w.append(a1[j])
        elif len(w) == n - 1:
            if a1[j] != w[j-1] and a1[j] != w[0]:
                w.append(a1[j])
            elif a2[j] != w[j-1] and a2[j] != w[0]:
                w.append(a2[j])
            elif a3[j] != w[j-1] and a3[j] != w[0]:
                w.append(a3[j])
        elif a1[j] != w[j-1]:
            w.append(a1[j])
        elif a2[j] != w[j-1]:
            w.append(a2[j])
        elif a3[j] != w[j-1]:
            w.append(a3[j])
    for i in w:
        print(i, end=" ")
    print()
        