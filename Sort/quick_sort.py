
def quick_sort(array, start, end):
    if start >= end:  # 원소가 한개인경우
        return
    pivot = start  # pivot은 배열의 첫번째 요소부터 시작
    left = start + 1
    right = end

    while left <= right:  # 왼쪽보다 오른쪽이 클때까지

        # pivot을 기준으로 왼쪽이 작은 데이터이면
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot을 기준으로 배열 오른쪽이 큰 데이터이면
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 만약 pivot을 기준으로 순차적으로 왔는데 엇갈리게 되면
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right - 1)  # start는 항상 0
    quick_sort(array, right + 1, end)  # end는 항상 array 끝


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array)-1)
print(array)
