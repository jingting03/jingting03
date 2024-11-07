N = int(input())  # 讀入正整數 N

# 初始化空列表來存儲奇數
odd_numbers = []

# 遍歷 1 到 N 之間的數字
for i in range(1, N+1):
    if i % 2 != 0:  # 判斷是否為奇數
        odd_numbers.append(str(i))  # 把奇數轉為字串並加入列表

# 用空格連接並打印所有奇數
print(" ".join(odd_numbers))
