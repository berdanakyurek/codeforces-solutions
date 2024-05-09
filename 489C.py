
def solve(m, s):
    #print(m, s)
    if s > 9*m:
        print("-1 -1")
        return
    if s == 0:
        if m == 1:
            print("0 0")
        else:
            print("-1 -1")
        return

    minimum = 1
    for i in range(m-1):
        minimum *= 10
    maximum = minimum * 10 -1
    #print(minimum, maximum)

    sumMin = s
    mCopy = m
    maxArr = []
    for i in range(m):
        maxArr.append(0)

    index = 0
    while sumMin > 0:
        maxArr[index] += 1
        sumMin -= 1
        if maxArr[index] == 9:
            index += 1

    sumMin = s
    mCopy = m
    minArr = []
    for i in range(m):
        minArr.append(0)

    minArr[0] += 1
    sumMin -= 1
    index = m - 1
    while sumMin > 0:
        minArr[index] += 1
        sumMin -= 1
        if minArr[index] == 9:
            index -= 1

    for i in minArr:
        print(i, end="")

    print(" ", end="")
    for i in maxArr:
        print(i, end="")
    print()

l = input().split()

solve(int(l[0]), int(l[1]))
