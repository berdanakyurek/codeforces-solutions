t = int(input())

for i in range(t):
    n = int(input())
    arr = [ int(x) for x in input().split() ]
    arr.sort()

    turn = False # Alice, even
    pAlice = 0
    pBob = 0
    while len(arr) != 0:
        biggest = arr[-1]

        arr.pop(-1)

        if biggest % 2 == 0 and turn == False:
            pAlice += biggest
        if biggest % 2 == 1 and turn == True:
            pBob += biggest

        turn = not turn
        #break
    
    if pAlice > pBob:
        print("Alice")
    elif pAlice < pBob:
        print("Bob")
    else:
        print("Tie")
    