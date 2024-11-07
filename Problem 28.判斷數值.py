N = int(input())

if N % 2 == 0:
    result = "even"
else:
    result = "odd"

is_prime = True

if N <= 1:
    is_prime = False
else:
    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{result} prime")
else:
    print(result)
