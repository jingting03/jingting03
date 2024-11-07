# 第一行輸入一個整數 N
N = int(input())

# 第二行輸入 N 個整數，數字間用空白隔開
numbers = input().split()
numbers = [int(num) for num in numbers]

# 第三行輸入一個整數 M
M = int(input())

# 將 M 加入數字列
numbers.append(M)

# 對數字列進行遞升排序
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

# 輸出排序後的結果，用逗號隔開
print(",".join(str(num) for num in numbers))
