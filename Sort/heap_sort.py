## 힙정렬 : 이진 트리 구조로 구성 
def solve():
    array = [230, 10, 60, 550, 40, 220, 20]

    heapSort(array)

    print(array)


def heapify(array, n, i):
    point = i
    left = i * 2 + 1
    right = i * 2 + 2

    if (left < n and array[point] < array[left]):
        point = left

    if (right < n and array[point] < array[right]):
        point = right

    if (i != point):
        swap(array, point, i)
        heapify(array, n, point)


def heapSort(array):
    n = len(array)

    for i in range(int(n/2-1), 0, -1):
        heapify(array, n, i)

    # for extract max element from heap

    for i in range(n-1, 1, -1):
        swap(array, 0, i)
        heapify(array, i, 0)


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


solve()
