# counting sort 구현

### counting 정렬의 첫번째는 array는 array에 넣어진 최대 숫자 (max) 만큼의 길이가 생성된다. 

def counting_sort(array, max):

    # counting array 생성
    counting_array = [0]*(max+1)

    # counting array에 input array내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1

    # counting array 업데이트. # 나중에 정렬할 때 해당 index에 넣기 위해서 총 데이터의 개수를 알아본다. 
    # 전 index에 해당되는 값을 더해서 나온 결과는 지금까지 데이터가 몇개 있는 지를 알 수 있고 
    # 나중에 정렬할 때 데이터 크기 에 해당되는 index에 결과값을 저장하기 위해서 
    for i in range(max):
        counting_array[i+1] += counting_array[i]

    # output array 생성
    output_array = [-1]*len(array)

    # output array에 정렬하기(counting array를 참조)
    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
        
    return output_array

