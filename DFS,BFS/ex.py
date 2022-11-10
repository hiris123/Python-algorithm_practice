N,M = map(int,input().split())

list1=[]
for _ in range(N):
    list1.append(list(map(int,input())))

def dfs(i,j):
    ix = [-1,1,0,0]
    iy = [0,0,-1,1]
    
    if i <= -1 or i >=N or j <= -1 or j >= M:
        return False 
    
    if list1[i][j] == 0:
        list1[i][j] = 1
        
        dfs(i+ix[0],j+iy[0])
        dfs(i+ix[1],j+iy[1])
        dfs(i+ix[2],j+iy[2])
        dfs(i+ix[3],j+iy[3])
        return True 
    
    return False 
    
cnt = 0 
for x in range(N):
    for y in range(M):
        if dfs(x,y) == True:
            cnt +=1 
print(cnt)