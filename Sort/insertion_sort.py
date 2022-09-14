def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]  # temp에 인덱스를 임시로 저장
        prev = i - 1  # 해당 인덱스의 끝-1 부터 시작 ( 뒤에서 부터 시작)
        while (prev >= 0 and arr[prev] > temp):  # 제대로 정렬이 되어있지 않다면
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev+1] = temp

    return arr


print(insertion_sort([0, 3, 4, 1, 2, ]))
