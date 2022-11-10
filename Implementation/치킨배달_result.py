import sys
from itertools import combinations

N, M = map(int, input().split())

city = []
for _ in range(N):
    city.append(list(map(int, input())))

# chicken = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 2]
# house = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 1]


home = []
chicken = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            home.append((x, y))
        if city[x][y] == 2:
            chicken.append((x, y))
        else:
            continue

minimum = 1e9

for case in combinations(chicken, M):
    total = 0
    for i in range(len(home)):
        mid_sum = 1e9
        for c in case:
            print(case)
            mid_sum = min(mid_sum, abs(home[i][0] - c[0]) + abs(home[i][1] - c[1]))
						
        total += mid_sum
    if total < minimum:
        minimum = total

print(minimum)