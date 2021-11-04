number_of_lines = int(input())
    
for i in range(number_of_lines):
    input()
    arr = input().split()
    
    no_ret = 0
    
    for j in range(len(arr)):
        if j + 1 + no_ret < int(arr[j]):
            no_ret += int(arr[j]) - j - 1 - no_ret
     