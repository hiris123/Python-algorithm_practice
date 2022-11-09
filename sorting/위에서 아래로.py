
n = int(input())
list1 = [int(input()) for _ in range(n)]

for x in range(n):
    for j in range(x, n):
        if list1[x] > list1[j]:
            list1[x], list1[j] = list1[j], list1[x]

print(list1)
