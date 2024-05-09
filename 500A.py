
s = input().split()
n = int(s[0])
t = int(s[1]) - 1


cells = input().split()
place = 0

while place < t:
    place += int(cells[place])

if place == t:
    print("YES")
else:
    print("NO")
