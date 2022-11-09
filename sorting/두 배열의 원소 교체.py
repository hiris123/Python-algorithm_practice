
N, K = input().split()
N = int(N)
K = int(K)

A = list(map(int, input().split()))
B = list(map(int, input().split()))


# 계수 정렬로 구현해보기

count = [0] * (max(A)+1)

for x in A:
    count[x] += 1

count1 = []
for x in range(len(count)):
    for i in range(count[x]):
        count1.append(x)
print(count1)

# 계수 정렬로 B 정렬

count = [0] * (max(B)+1)

for x in B:
    count[x] += 1

count2 = []
for x in range(len(count)):
    for i in range(count[x]):
        count2.append(x)

print(count2)

for x in range(K):
    count1[x] = count2[N-x-1]

sum = 0
for x in range(N):
    sum += count1[x]
print(sum)
