## 수 정렬하기 3 ## 


n = int(input())
nums = [int(input()) for _ in range(n)]

# dictionary 형태로 먼저 만든다. 
nums_dic = {}
for x in nums: 
    if x in nums_dic.keys(): 
        nums_dic[x] += 1 
        continue
    nums_dic[x] = 1 

print(nums_dic) ## {2: 2, 4: 1, 3: 1, 1: 1}


nums_keys  = list(nums_dic.keys())

# 삽입 정렬 
for x in range(len(nums_keys)):
    temp = nums_keys[x]
    prev = x - 1 
    while (prev >= 0 and nums_keys[prev] >temp):
        nums_keys[prev + 1] = nums_keys[prev]
        prev -= 1 
    nums_keys[prev+1] = temp

print(nums_keys) # [1, 2, 3, 4]

final_nums = []
for x in nums_keys:
    for j in range(nums_dic[x]):
        final_nums.append(x)

for a in final_nums:
    print(a)