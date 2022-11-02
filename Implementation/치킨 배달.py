

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

home_list = []
chicken_list = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            home_list.append((x, y))
        if graph[x][y] == 2:
            chicken_list.append((x, y))
        else:
            continue


total_sum = 0
min_list = []
for (x, y) in home_list:
    min1 = 100
    temp = 0
    for (x1, y1) in chicken_list:
        sum = 0
        sum += abs(x-x1)
        sum += abs(y-y1)
        min1 = min(min1, sum)
        if (min1 == sum):
            temp = [x1, y1, sum]
    min_list.append(temp)
print(min_list)

min = [0] * M

for i in range(len(min_list)):  # i : 0 / j:12,3, / i=1, j:2,3/ i =2 j : 3


final_list = []
for i in range(len(min_list)):  # i : 0 / j:12,3, / i=1, j:2,3/ i =2 j : 3
    for j in range(i+1, len(min_list)):  # j 1,2,3,
        if (min_list[i][0] == min_list[j][0] and min_list[i][1] == min_list[j][1]):
            min_list[i][2] += min_list[j][2]

######### 중복 제거 ########

for i in range(len(min_list)):  # i : 0 / j:12,3, / i=1, j:2,3/ i =2 j : 3
    for j in range(i+1, len(min_list)):  # j 1,2,3,
        if (min_list[i][0] == min_list[j][0] and min_list[i][1] == min_list[j][1]):
            min_list[i][2] < min_list[j][2]

print(new_list)
