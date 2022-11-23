N,M = map(int,input().split())
array = [int(input()) for _ in range(N)]
print(array)
def array1(M,i):
    value = True
    for x in range(N-1,0,-1):
        if M == 0 :
            print(i)
            return i 
        if (M % array[x] == 0) :
            M -= array[x]
            value = False 
            i += 1
            array1(M,i)
    if value:
        print(-1)
        return 0 
   

array1(M,0)