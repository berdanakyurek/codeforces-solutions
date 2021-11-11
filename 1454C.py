def solve(arr, lenn):
    if lenn <= 1:
        return 0
    flag = False

    dic = {}

    flag2 = False
    seqStart = -1
    for i in range(len(arr)):
        toAdd = 1
        if arr[i] != arr[0]:
            flag = True
        flag2 = True
        seqStart = arr[i]

        if i == 0 or arr[i-1] == arr[i] or i == len(arr) - 1 :
            toAdd = 0

        if str(arr[i]) in dic:
            dic[str(arr[i])] += toAdd
        else:
            dic[str(arr[i])] = toAdd

    if arr[-1] == arr[-2] and dic[str(arr[i])] >= 0 :
        dic[str(arr[i])] -= 1

    if not flag:
        return 0

    mins = []
    minCount = -1

    for i in dic:
        if dic[i] < minCount or minCount == -1:
            mins = []
            mins.append(int(i))
            minCount = int(dic[i])
        elif dic[i] == minCount:
            mins.append(int(i))

    return minCount + 1

t = int(input())
for i in range(t):
    x = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr, x ))
