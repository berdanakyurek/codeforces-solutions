import heapq

class Q_item:
    def __init__(self, social, no):
        self.social = social
        self.no = no

    def __lt__(self, other):
        if self.social > other.social:
            return True
        return False


t = int(input())

for i in range(t):
    number_of_people = int(input())
    people = [int(part) for part in input().split()]
    pq = []

    for j in range(len(people)):
       heapq.heappush(pq, Q_item(people[j], j+1))
    total = 0
    meetings = []
    while True:
        p1 = heapq.heappop(pq)
        p2 = heapq.heappop(pq)

        if p1.social <= 0 or p2.social <= 0:
            break

        total += 1
        meetings.append([p1.no, p2.no])
        p1.social -= 1
        p2.social -= 1
        heapq.heappush(pq, p2)
        heapq.heappush(pq, p1)


    print(total)
    for m in meetings:
        print(m[0], m[1])
