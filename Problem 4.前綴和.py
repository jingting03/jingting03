# 輸入陣列大小N
N = int(input())

# 輸入陣列A的元素
A = list(map(int, input().split()))

# 初始化前綴和陣列B
B = []
current_sum = 0

# 計算前綴和
for num in A:
    current_sum += num
    B.append(current_sum)

# 輸出陣列B
print(" ".join(map(str, B)))
