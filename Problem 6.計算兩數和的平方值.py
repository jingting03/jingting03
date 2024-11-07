# 讀取測試案例數量
n = int(input())

# 處理每組測試案例
for _ in range(n):
    # 讀取每組的兩個整數
    a, b = map(int, input().split())
    
    # 計算和的平方
    result = (a + b) ** 2
    
    # 輸出結果並確保每行有換行符號
    print(result)
