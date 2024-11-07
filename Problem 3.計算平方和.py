numbers = input().split() 

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

square_sum = 0  
for num in numbers:
    square_sum += num ** 2 

print(square_sum)  
