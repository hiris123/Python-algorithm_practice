import sys 
N = int(input())
array = [int(input()) for _ in range(N)]

## 정렬 ## 
array.sort() 

## 메인 코드 ## 

# 가장 작은 값 2개를 더해서 넣는다. 이를 반복한다. 

temp = []
for j in range(len(array)):
    if j % 2 == 1:
        temp.append(array[j-1]*2 +array[j] *2)
    if j % 2 == 0 and j == len(array) - 1 :
        temp.append(array[j])
print(temp)
def arrays(array):
    if len(array) <=1:
        print(array[0])
        return array[0]
    
    array1=[]
    for j in range(len(array)):
        if len(array) == 2:
            print(array[0]  + array[1])
            return array[0]  + array[1]
        if j % 2 == 1 :
            array1.append(array[j-1] * 2 + array[j] * 2)
    array1.sort() # 작은 값 두개 씩 더해야 하므로 정렬을 한 번 더한다. 
    arrays(array1)
    
arrays(temp)