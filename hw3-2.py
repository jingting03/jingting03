num = int(input())
total_sum = 0

for i in range(1, num + 1):
    if i % 4 == 0:
        total_sum += i

print(total_sum)

