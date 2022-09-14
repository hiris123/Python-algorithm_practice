
# 병합 정렬 : 각 정렬된 숫자들을 1개의 정렬된 숫자들로 합치는 것

def merge_sort(arr):

    def sort(low, high):

        if high - low < 2:
            return
        mid = (low + high) // 2  # 중간값 생성
        sort(low, mid)

        sort(mid, high)

        merge(low, mid, high)

    def merge(low, mid, high):
        # 첫번째 mid는 1 low는 0  high는 2
        print(mid, low, high, "mid", "low", "high")
        temp = []
        l, h = low, mid

        while l < mid and h < high:  # low < mid , mid < high
            if arr[l] < arr[h]:

                temp.append(arr[l])
                l += 1
            else:

                temp.append(arr[h])
                h += 1

        while l < mid:

            temp.append(arr[l])
            l += 1
        while h < high:

            temp.append(arr[h])
            h += 1

        for i in range(low, high):  # 정렬된 merged를 원래의 배열인 list에 넣는다.
            arr[i] = temp[i - low]

    return sort(0, len(arr))  # 제일 먼저 실행


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
merge_sort(array)
print(array)
