
def bubbleSort(arr): 
    
    temp = 0
    
    for i in range(0, len(arr)):
        for j in range(1,len(arr) -i):
            if(arr[j-1] >  arr[j]):
               temp = arr[j-1]
               arr[j-1] = arr[j]
               arr[j] = temp
                
    return arr


print(bubbleSort([0,3,1,2]))

