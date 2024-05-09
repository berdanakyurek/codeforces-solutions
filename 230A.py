class Dragon:
    def __init__(self, strength, bonus):
        self.strength = strength
        self.bonus = bonus
    
splitted = input().split()

s = int(splitted[0])
n = int(splitted[1])


dragons = []
for i in range(n):
    line = input().split()
    dragon = Dragon(int(line[0]), int(line[1]))
    dragons.append(dragon)
    
dragons.sort(key=lambda x: x.strength)

for dragon in dragons:
    if s <= dragon.strength:
        print("NO")
        exit()
    s += dragon.bonus
print("YES")
