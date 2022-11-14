def solution(N, stages):
    
    
    
    count = [0] * (N + 2)
    for i in stages:
        count[i] += 1 
    print(count)
    
    answer=[]
    people = sum(count)
    for x in range(len(count)):
        
        if x == 0 :
            continue 
        if x == 6:
            break
        if count[x] == 0 :
            answer.append((x,0))
        
        else:
            print(count[x], people)
            a = count[x] / people
            
            answer.append((x,a))
            people -= count[x]
    
    answer = sorted(answer, key=lambda x : x[1],reverse=True) 
       
    answer1=[]
    for x in answer:
        answer1.append(x[0])
        
    return answer1

print(solution(5,[2,1,2,6,2,4,3,3]))