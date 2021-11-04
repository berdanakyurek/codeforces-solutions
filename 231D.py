
location = [int(x) for x in input().split()]
oppositeVertex = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

x = location[0]
y = location[1]
z = location[2]

sum = 0

if y < 0:
    sum += numbers[0]
if y > oppositeVertex[1]:
    sum += numbers[1]

if z < 0:
    sum += numbers[2]
if z > oppositeVertex[2]:
    sum += numbers[3]

if x < 0:
    sum += numbers[4]
if x > oppositeVertex[0]:
    sum += numbers[5]

print(sum)
