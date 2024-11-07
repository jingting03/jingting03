n = int(input(""))  
numbers = []

for i in range(n):
    num = input()
    numbers.append(num) 

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

max_number = ''
for num in numbers:
    max_number += num

print(max_number)
