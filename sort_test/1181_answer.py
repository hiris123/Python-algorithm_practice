
n = int(input())
a = []
for i in range(0,n):
    a.append(input())
    
a = list(set(a))
a.sort() # 단어 순서대로 
a.sort(key=len) # 길이 순서대로 

for i in a:
    print(i)