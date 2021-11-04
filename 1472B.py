def check(n, lst):
    
    count1 = lst.count(1)
    count2 = n - count1
    sum = count1 + 2 * count2
    if sum % 2 != 0:
        return "NO"

    if count2 % 2 != 0:
        if count1 < 2:
            return "NO"
        count2 += 1
        count1 -= 2
    
    if count1 % 2 != 0:
        return "NO"
    return "YES"
        

t = int(input())

for i in range(t):
    n = int(input())
    lst =  list(map(int, input().split()))
    print(check(n, lst))