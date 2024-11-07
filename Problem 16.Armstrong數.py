N = int(input())  # 输入三位数的正整数 N

# 拆解三位数的各个数字
hundreds = N // 100
tens = (N // 10) % 10
ones = N % 10

# 计算各位数字的立方和
if hundreds**3 + tens**3 + ones**3 == N:
    print("YES")
else:
    print("NO")
