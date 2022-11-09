n = int(input())

list1 = [input().split() for _ in range(n)]


def setting(array):
    return array[1]


result = sorted(list1, key=setting)

for x in result:
    print(x[0], end=" ")
