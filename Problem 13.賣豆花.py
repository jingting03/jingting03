
amount = int(input())

hundreds = amount // 100
amount %= 100

tens = amount // 10
amount %= 10

ones = amount

print(f"百元 {hundreds}")
print(f"十元 {tens}")
print(f"壹元 {ones}")
