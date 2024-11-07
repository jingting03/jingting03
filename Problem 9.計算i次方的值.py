# 讀取測試案例數量
n = int(input())

# 處理每組測試案例
for _ in range(n):
    # 讀取整數 i
    i = int(input())
    
    # 判斷並輸出結果
    if i > 31:
        print("Value of more than 31")
    else:
        print(2 ** i)
