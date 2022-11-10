def solution(food_time, k):
    
    food_times=[]
    for x in food_time:
        
        food_times.append(int(x))
    

    num = 0
    i = 0 
    list1=[1] * (len(food_times) -1 )
    for x in range(k):

        if (i == len(food_times) -1 ):
            i = 0
        
        if (food_times[i] == 0):
            list1[i] = 0
            i += 1 
            continue
        
        food_times[i]  -= 1
        i += 1 

        if(x != k-1 ):
            if 1 in list1:
                return -1 
    
    
    
    
    return i

print(solution([3,1,2],5))


def solution(food_time, k):
    
    food_times=[]
    for x in food_time:
        
        food_times.append(int(x))
    

    list1=[]
    num = 0
    i = 0 
    for x in range(k):

        if (i == len(food_times) -1 ):
            i = 0

        if (food_times[i] == 0):
            i += 1 
            continue
        food_times[i]  -= 1
        i += 1 
        
        if(x != k-1 ):
            if 1 not in list1:
                return -1 
    
    
    
    
    return i