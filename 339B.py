def calculate_cost(n, place, dest):
    if dest >= place:
        return dest - place
    return n - place + dest
    
n = int(input().split()[0])

cost = 0
place = 1

for dest in input().split():
    dest = int(dest)
    cost += calculate_cost(n, place, dest)
    place = dest
print(cost)
