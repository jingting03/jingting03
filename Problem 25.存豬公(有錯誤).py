S = int(input())

n = int(input())
total_savings = 0

for day in range(n):
    total_savings += S * (2 ** day)

print(f"第{n}天共存{total_savings}元")
