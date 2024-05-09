n = int(input())

t1 = 0
t1_name = None

t2 = 0
t2_name = None


for i in range(n):
    name = input()
    if t1_name == None:
        t1_name = name
    if t1_name == name:
        t1 += 1
    else:
        t2_name = name
        t2 += 1

if t1 > t2:
    print(t1_name)
else:
    print(t2_name)
