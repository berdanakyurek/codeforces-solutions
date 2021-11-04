def is2pow(n):
    
    i = 0
    while True:
        if 2 ** i == n:
            return True
        elif 2 ** i > n:
            return False
        i += 1

def compute(f, s):

    if f == s:
        return 0
    
    if f > s: 
        temp = s
        s = f
        f = temp
    
    if not s % f == 0:
        return -1

    #if not is2pow(s / f):
    #    return -1
    
    move = 0
    
    while True:
        if s/f >= 8:
            f *= 8
        elif s/f >= 4:
            f *= 4
        elif s/f >= 2:
            f *= 2
        else:
            return -1
        move += 1

        if  s == f:
            return move

N = int(input())
for i in range(N):
    line = input().split()

    print(compute(int(line[0]),int(line[1])))