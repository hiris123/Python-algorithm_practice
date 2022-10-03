n = int(input())

sum = 0


while (n >= 500):
    n_copy = n
    n_copy = n_copy // 500
    n = n % 500
    sum += n_copy
while (n >= 100):
    n_copy = n
    n_copy = n_copy // 100
    n = n % 100
    sum += n_copy

while (n >= 50):
    n_copy = n
    n_copy = n_copy // 50
    n = n % 50
    sum += n_copy

while (n >= 10):
    n_copy = n
    n_copy = n_copy // 10
    n = n % 10
    sum += n_copy

print(sum)
