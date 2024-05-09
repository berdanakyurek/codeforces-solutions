sums = [0, 0, 0]
for i in range(int(input())):
    splitted = input().split()
    for i in range(len(splitted)):
        sums[i] += int(splitted[i])

if sums[0] == 0 and sums[1] == 0 and sums[2] == 0:
    print("YES")
else:
    print("NO")
