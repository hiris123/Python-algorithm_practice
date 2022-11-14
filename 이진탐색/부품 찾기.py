import sys
N = int(sys.stdin.readline())
my_data = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
person_data = list(map(int,sys.stdin.readline().split()))

print(N, my_data,M,person_data)


def check(array, i, start, end):
    while (start < end):
        target = (start + end) // 2 
        if array[target]  == i:
            return "yes"
        elif array[target] > i : 
            end = target -1 
        else :
            start = target + 1 
    
    return None
            
    

# 1. 배열 정렬 ( 삽입 정렬로 수행 )

for i in range(len(my_data)):
    for x in range(i,0,-1):
        if my_data[x] > my_data[i] : 
            my_data[x] , my_data[i] = my_data[i], my_data[x]
        




# 이진 탐색으로 해당 데이터가 있는지 확인 

# check 이라는 메소드에 인자를 넣어 해당 인자가 있는 지 없는 지에 대한 여부 확인 
end = N 
for i in person_data:
    if check(my_data,i,0,N) == None:
        print("No", end=" ")
    else:
        print("Yes",end=" ")