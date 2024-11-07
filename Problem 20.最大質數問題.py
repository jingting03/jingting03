# 输入一个正整数
n = int(input())

# 从 n-1 开始，逐个向下检查是否是质数
for i in range(n - 1, 1, -1):
    is_prime = True  # 假设 i 是质数

    # 检查 i 是否是质数
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False  # 如果 i 能被 j 整除，则不是质数
            break
    
    # 如果是质数，则输出并结束
    if is_prime:
        print(i)
        break
