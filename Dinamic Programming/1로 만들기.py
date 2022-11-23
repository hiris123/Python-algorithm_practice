
N = int(input())


def makeOne(N,i):
    if (N == 1):
        print("최종", i)
        return 0
    elif (N % 5 == 0 ):
        N //= 5 
        i += 1 
        
        makeOne(N,i)
    elif (N % 3 == 0 ):
        N //= 3 
        i += 1 
       
        makeOne(N,i)
        
    elif (N % 2 == 0 ):
        N //= 2 
        i += 1 
        
        makeOne(N,i)
    else:
        N -= 1 
        i += 1 
  
        makeOne(N,i)

makeOne(N,0)

