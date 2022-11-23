N = int(input())

array = [(1,2),(2,1),(2,2)]


d = [0] * 10001 
d[1] = 0 
d[2] = 3
for i in range(3, N+1):
    
    d[i] = d[i-2] *2 + d[i-1] 
    
print(d[N])