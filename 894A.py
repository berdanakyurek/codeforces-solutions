x = input()

if x == "":
    print(0)
    exit()
y = ""

for i in x:
    if i == "Q" or i == "A":
        y += i

if y == "":
    print(0)
    exit()

while len(y) > 0 and y[0] == "A" :
    y = y[1:]
    

if y == "":
    print(0)
    exit()

while len(y) > 0 and y[-1] == "A" :
    y = y[:-1]

if y == "":
    print(0)
    exit()

totalNo = 0
for i in range(len(y)):
    for j in range(i + 1,len(y)):
        if y[i] == "Q" and y[j] == "Q":
            for k in range(i,j):
                if y[k] == "A":
                    totalNo += 1 
print(totalNo)