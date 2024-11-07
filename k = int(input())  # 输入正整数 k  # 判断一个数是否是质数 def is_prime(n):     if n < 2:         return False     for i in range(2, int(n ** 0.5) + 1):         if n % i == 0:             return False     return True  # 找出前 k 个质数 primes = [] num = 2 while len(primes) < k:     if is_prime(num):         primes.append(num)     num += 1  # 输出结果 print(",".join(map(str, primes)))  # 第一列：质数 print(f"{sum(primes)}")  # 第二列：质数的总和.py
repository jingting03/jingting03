k = int(input())  # 输入正整数 k

# 判断一个数是否是质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出前 k 个质数
primes = []
num = 2
while len(primes) < k:
    if is_prime(num):
        primes.append(num)
    num += 1

# 输出结果
print(",".join(map(str, primes)))  # 第一列：质数
print(f"{sum(primes)}")  # 第二列：质数的总和
