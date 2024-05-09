import copy

def from_left(splitted):
    left = int(splitted[0])
    
    while int(splitted[0]) == left:
        splitted.pop(0)
        if len(splitted) == 0:
            return 0
        
    while int(splitted[-1]) == left:
        splitted.pop()
        if len(splitted) == 0:
            return 0
    return len(splitted)

def solve(a):
    splitted = a.split()

    if len(splitted) == 1:
        return 0
    
    sorted = copy.deepcopy(splitted)
    sorted.sort()

    if sorted[0] == sorted[-1]:
        return 0
    if sorted[0] == sorted[-2]:
        return 1
    if sorted[1] == sorted[-1]:
        return 1
    
    if splitted[0] == splitted[-1]:
        return from_left(splitted)

    left_count = 0
    left_flag = True
    right_count = 0
    right_flag = True
    
    for i in range(len(splitted)):
        if left_flag:
            if splitted[i] == splitted[0]:
                left_count += 1
            else:
                left_flag = False
                
        if right_flag:
            if splitted[(-1 * i) - 1] == splitted[-1]:
                right_count += 1
            else:
                right_flag = False
        if left_flag is False and right_flag is False:
            break
        
    return len(splitted) - max(left_count, right_count)



n = int(input())
 
for i in range(n):
    input()
    print(solve(input()))
