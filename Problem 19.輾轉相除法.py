m, n = input().split()
m = int(m)
n = int(n)

while n != 0:
    m, n = n, m % n

print(m)
