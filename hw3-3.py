n=int(input())
prime_numbers = []

for number in range(2, n + 1):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)

prime_numbers.reverse()

print(prime_numbers)



