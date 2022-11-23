N = int(input())
array = list(map(int, input().split()))


# 앞선 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0] * 30001
d[0] = array[0]
d[1] = max(d[0],array[1])

for i in range(2,N):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[N-1])
