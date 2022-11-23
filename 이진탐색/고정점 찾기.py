
N = int(input())
array = list(map(int,input().split()))

print(array)
def SameIndex(array):
    start = 0 
    end = len(array)
    
    pivot = (start + end ) // 2 
    check = True
    while(start <= end ):
        pivot = (start + end ) // 2 
   
        if array[pivot] == pivot : 
            check = False
            return pivot 
        elif array[pivot] > pivot : 
       
            end = pivot -1 
        elif array[pivot] < pivot : 
            start = pivot + 1 
    if check:
        return -1 
print(SameIndex(array))