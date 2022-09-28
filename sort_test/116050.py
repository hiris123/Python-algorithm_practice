

n = int(input())
nums = []
for _ in range(n):
    a, b = map(int, input().split())
    nums.append((a, b))


for x in range(n):
    temp = nums[x]
    prev = x - 1
    while (prev >= 0 and nums[prev][0] >= temp[0]):
        if nums[prev][0] == temp[0]:
            if nums[prev][1] > temp[1]:
                nums[prev+1] = nums[prev]
                prev -= 1
                continue
            else:
                break
        nums[prev+1] = nums[prev]
        prev -= 1
    nums[prev + 1] = temp
print(nums)
