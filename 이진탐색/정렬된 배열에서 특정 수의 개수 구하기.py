
N,x = map(int,input().split())
array = list(map(int,input().split()))


def checked(array):
    start = 0
    end = len(array)-1 
    target = 0 
    check = True 
    while(start <= end):
        
        pivot = (start + end ) // 2 
        
        if array[pivot] > x : 
            end = pivot -1 
        if array[pivot] < x :
            start = pivot + 1 
        if array[pivot] == x :
            target = pivot 
            check = False 
            return target 
            
    if check:
        return -1 

if checked(array) == -1 :
    print(-1)
else:
    target = checked(array)
    sum = 0 
    pk = target 
    for i in range(len(array)):
        if array[target] != x:
            
            break 
        elif array[target] == x :
            sum +=1 
            target -= 1
            

    for i in range(len(array)):
        if array[pk] != x:
            break 
        elif array[pk+1] == x :
            sum +=1 
            pk += 1

    print(sum)