import sys 
N,M = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))



## 떡 자르기 

def cut(M,ricecake):
    if ricecake >= M:
        return ricecake-M
    else:
        return 0


## 잘린 떡의 길이만큼 합치기 

list1=[]
for i in range(0,max(array)): # 0 부터 해당 배열의 최고값까지 범위를 돌리기 
    sum = 0 # 처음부터 돌려서 list1에 sum 값을 넣기 
    for ricecake in array:  
        sum += cut(i,ricecake) 
    if sum == 6 :
        list1.append(i)
print(max(list1)) # list1에 해당 max 값 print 하기 