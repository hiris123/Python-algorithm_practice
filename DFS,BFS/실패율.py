def solution(N, stages):
    
    
    ## counting 정렬로 [2,1,2,6,2,4,3,3] -> [0,1,3,2,1,0,1] ###
    count = [0] * (N + 1)
    for i in stages:
        if (i >= len(count)): # 만약 i가 6이면 5를 통과했다는 의미이므로 5에는 0명이 있을 것이다. 그래서 해당 인덱스는 count 하지 않고 넘어간다. 
            continue
        
        count[i] += 1 
    print(count)
    #########################
    answer=[]
    people = len(stages)

    for x in range(len(count)):
        
        
        if x == 0 :
            continue 
        if count[x] == 0 :
           
            answer.append((x,0))
        
        else:
            
            a = count[x] / people
            
            answer.append((x,a))
            people -= count[x]
    
    answer = sorted(answer, key=lambda x : x[1],reverse=True) # 2번째 인덱스 기준으로 정렬을 한다. 

    answer1=[]
    for x in answer:
        answer1.append(x[0])
        
    return answer1

print(solution(5,[2,1,2,6,2,4,3,3]))