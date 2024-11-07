# 讀取通話分鐘數
minutes = int(input())

# 計算費用
if minutes <= 800:
    cost = minutes * 0.9
elif minutes < 1500:
    cost = minutes * 0.9 * 0.9  # 9折
else:
    cost = minutes * 0.9 * 0.79 # 79折

# 輸出結果，取到小數點以下第一位
print(f"{cost:.1f}")
