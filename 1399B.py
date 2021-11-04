t = int(input())
for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    mnC = min(candies)
    mnO = min(oranges)
 
    move = 0
    for i in range(n):

        if candies[i] > mnC and oranges[i] > mnO:
            hamle = min(candies[i]-mnC, oranges[i]-mnO)
            oranges[i] -= hamle
            candies [i] -= hamle
            move += hamle
        
        if candies[i] > mnC:
            hamle = candies[i] - mnC
            candies[i] -= hamle
            move += hamle
        
        if oranges[i] > mnO:
            hamle = oranges[i] - mnO
            oranges[i] -= hamle
            move += hamle

    
    print(move)

    
    