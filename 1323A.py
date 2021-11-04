for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    tek1 = -1
    tek2 = -1
    cift = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            cift = i + 1
            break
        else:
            if tek1 == -1:
                tek1 = i + 1
            else:
                tek2 = i + 1
                break

    if cift != -1:
        print(1)
        print(cift)
    elif tek2 != -1:
        print(2)
        print(tek1, tek2)
    else:
        print(-1)