
### 수 정렬하기 ###
### N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오 

print("안녕하세요")
n = int(input())
nums = [int(input()) for _ in range(n)]

for x in range(n): 
    big = nums[0]
    temp = 0 
    index = 0 
    for j in range(0,n-x):
        if nums[j] > big:
            big = nums[j]
            index = j 
    temp = nums[n-x-1]        
    nums[n-x-1] = big
    nums[index] = temp 

i = 0 
for x in range(n): 
    print(nums[i])
    i += 1 