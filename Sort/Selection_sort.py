def selection_sort(arr):
    temp = 0 
    for i in range(len(arr)):
        indexMin = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indexMin]:
                indexMin = j 
        temp = arr[indexMin]
        arr[indexMin] = arr[i]
        arr[i] = temp
    
    
    return arr


print(selection_sort([0,3,1,2]))