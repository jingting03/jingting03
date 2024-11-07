inputs = input().split()
A = int(inputs[0])
B = int(inputs[1])
C = int(inputs[2])

total_sum = A + B + C

if total_sum > 9:
    result = "H"
else:
    result = "L"

print(total_sum, result)
