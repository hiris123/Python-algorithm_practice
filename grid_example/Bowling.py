
import time

N, M = map(int, input().split())

data = list(map(int, input().split()))

## 정렬을 한다. 

start = time.time()
data.sort()


list1= [0] * N

k = 0 

n = 1
for x in range(len(data) -1):
    if (data[x] == data[x+1]):
        n += 1 
        if (x == len(data) -2):
            list1[x+1] = n
        else:
            pass
    else:
        list1[x] = n
        n = 1 

list1.sort()
sum = 0 
for x in range(len(list1)):
    for i in range(x+1,len(list1)):
        sum += list1[x] * list1[i]

end = time.time()
print(end-start)