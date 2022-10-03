N, K = map(int, input().split())

sum = 0
while (N > 1):
    if (N % K == 0):
        N = N // K
        sum += 1
    else:
        N -= 1
        sum += 1

print(sum)
