N = int(input())

total_sum = 0

for num in range(1, N + 1):
    if num % 2 == 0 and num % 3 == 0 and num % 12 != 0:
        total_sum += num 

print(total_sum)
