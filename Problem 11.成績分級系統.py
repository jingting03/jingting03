# 讀取學生數量
n = int(input())

# 初始化各級別的計數器
excellent = 0  # 優等
first_class = 0  # 甲等
second_class = 0  # 乙等
third_class = 0  # 丙等
fail = 0  # 不及格

# 讀取每個學生的分數並進行分級
for _ in range(n):
    score = int(input())
    
    if 90 <= score <= 100:
        excellent += 1
    elif 80 <= score <= 89:
        first_class += 1
    elif 70 <= score <= 79:
        second_class += 1
    elif 60 <= score <= 69:
        third_class += 1
    elif 0 <= score <= 59:
        fail += 1

# 輸出每個等級的人數
print(f"優等 {excellent}")
print(f"甲等 {first_class}")
print(f"乙等 {second_class}")
print(f"丙等 {third_class}")
print(f"不及格 {fail}")
