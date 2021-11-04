n = int(input())

arr2 = input().split()
arr = []
for i in arr2:
    arr.append(int(i))

max = 1
counter = 1
for i in range(1, len(arr)) :
    if arr[i] > arr[i - 1]:
        counter += 1
    else:
        counter = 1
    if counter > max:
        max = counter

print(max)
