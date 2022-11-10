from collections import deque

N,M,K,X = map(int,input().split())
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

distance=[-1]*(N+1)
distance[X] = 0 

queue = deque([X])
while queue:
    node = queue.popleft()
    for x in graph[node]:
        if distance[x] != -1:
            distance[x] =  distance[node] + 1 
            queue.append(x)

check = False 
for city, dist in enumerate(distance):
    if dist == K:
        print(city, end =' ')
        check=True
if not check:
    print(-1)
