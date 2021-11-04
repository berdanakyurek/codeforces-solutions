def func(arr, n):
    c0 = arr.count(0)
    c1 = arr.count(1)
    c2 = arr.count(2)

    goal = int(n / 3)

    move = 0
    while c0 != goal or c1 != goal or c2 != goal:
        
        if c0 > goal:
            move += c0 - goal
            c1 += c0 - goal
            c0 = goal
        
        if c1 > goal:
            move += c1 - goal
            c2 += c1 - goal
            c1 = goal
        
        if c2 > goal:
            move += c2 - goal
            c0 += c2 - goal
            c2 = goal
        
    return move

t = int(input())

for qq in range(t):
    n = int(input())
    
    arr = []
    
    for i in input().split():
        arr.append(int(i) % 3)
    print(func(arr,n)) 