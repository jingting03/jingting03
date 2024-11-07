inputs = input().split()
M = int(inputs[0])
N = int(inputs[1])

for i in range(1, M + 1):
    for j in range(1, N + 1):
        print(f"{i}x{j}={i*j}")
