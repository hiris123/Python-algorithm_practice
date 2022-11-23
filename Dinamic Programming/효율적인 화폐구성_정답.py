# 정수 N M 을 입력받기 
n,m = map(int,input().split())
# N개의 화폐 단위 정보를 입력받기

array=[]
for i in range(n):
    array.append(int(input()))

d=[10001]*(m+1)

# 다이나믹 프로그래밍 진행 ( 보턴 업 )
d[0] = 0 
for i in range(n):
    for j in range(array[i], m+1): # array에 있는 요소들로부터 m+1 까지 1씩 증가하면서 돈다. 
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])