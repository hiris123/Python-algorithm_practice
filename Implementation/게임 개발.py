N, M = map(int, input().split())
x, y, dir = map(int, input().split())

list = []
list1 = []
for x in range(4):
    a, b, c, d = map(int, input().split())
    list1 = [a, b, c, d]
    list.append(list1)

print(list)
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 고려해야 할 상황
# 이미 간곳을 넣어야 할 리스트
#
if (dir == 0):
    dir = 4

dir += 1
num = 0
have_been_list = []
while (True):
    dir %= 4
    x += steps[dir][0]
    y += steps[dir][1]

    if (x < 0 or x > 3 or y < 0 or y > 3):
        x -= steps[dir][0]
        y -= steps[dir][1]
        dir += 1

    print(x, y)
    if (list1[x][y] == 0):
        if (x, y) not in have_been_list:
            have_been_list.append([x, y])
            dir += 1
            num += 1
        else:
            x -= steps[dir][0]
            y -= steps[dir][1]
            dir += 1
            pass

    else:
        x -= steps[dir][0]
        y -= steps[dir][1]
        dir += 1
