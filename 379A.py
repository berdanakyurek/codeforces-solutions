line = input().split()
a = int(line[0])
b = int(line[1])

hours = 0
burned = 0

while a > 0:
    hours += a
    burned += a
    a = burned // b
    burned -= a * b
print(hours)
