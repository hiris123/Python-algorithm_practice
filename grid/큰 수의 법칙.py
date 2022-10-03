N, K, M = map(int, input().split())
array = list(map(int, input().split()))

# 정렬 먼저 ## [ 삽입 정렬 사용 ]
for j in range(len(array)):
    temp = array[j]
    pivot = j - 1
    while (pivot > 0 and array[pivot] > temp):
        array[pivot + 1] = array[pivot]
        pivot -= 1
    array[pivot + 1] = temp

print(array)
answer = (K//M) * M * array[-1] + (K % M) * array[-2]
print(answer)
