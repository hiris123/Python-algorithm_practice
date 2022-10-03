H, L = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(L)]

small_list = []
for i in range(L):
    small = array[0][i]
    for k in range(H):
        if (array[k][i] <= small):
            small = array[k][i]
    small_list.append(small)

small_list.sort()
print(small_list[0])
