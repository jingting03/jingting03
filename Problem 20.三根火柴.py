inputs = input().split()
A = int(inputs[0])
B = int(inputs[1])
C = int(inputs[2])

if A >= B and A >= C:
    c, a, b = A, B, C
elif B >= A and B >= C:
    c, a, b = B, A, C
else:
    c, a, b = C, A, B


if a + b <= c:
    print("Not Triangle")  # 不满足三角形条件
elif a**2 + b**2 == c**2:
    print("Right Triangle")
elif a**2 + b**2 < c**2:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
