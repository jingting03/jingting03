# 第一行輸入整數 m 表示線段數量
m = int(input())

# 用於存儲所有的線段範圍
segments = []

# 輸入每條線段的端點
for _ in range(m):
    # 手動解析輸入並轉換為整數
    input_data = input().split()
    a = int(input_data[0])
    b = int(input_data[1])
    # 確保線段以小到大的順序存入
    segments.append((min(a, b), max(a, b)))

# 按起點排序線段
segments.sort()

# 計算覆蓋的總長度
total_length = 0
current_start, current_end = segments[0]

for start, end in segments[1:]:
    if start > current_end:
        # 沒有重疊，累加當前線段長度
        total_length += current_end - current_start
        current_start, current_end = start, end
    else:
        # 有重疊，更新結束點
        current_end = max(current_end, end)

# 最後一段累加進總長度
total_length += current_end - current_start

print(total_length)
