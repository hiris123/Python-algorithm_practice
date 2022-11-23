# 정수 X를 입력받기 

N,M = map(int,input().split())
array = [int(input()) for _ in range(N)]

d = [0]*10001
d[1] = 1
for i in range(2,M):
    d[i] = 10000
    for x in range(0,N):
        if d[i-array[x]] == 10000:
            continue 
        d[i] = min(d[i],d[i-array[x]]+1)
        print(d[i]) 

if d[N-1] == 10000:
    print(-1)
else:
    print(d[M-1])