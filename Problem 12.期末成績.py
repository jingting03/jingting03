# 输入学生人数
n = int(input())

# 初始化变量
scores = []
passing_count = 0

# 输入学生分数
for _ in range(n):
    score = int(input())
    scores.append(score)
    
    # 统计及格人数
    if score >= 60:  # 假设及格分数为60
        passing_count += 1

# 计算最高分、最低分和平均分
max_score = max(scores)
min_score = min(scores)
average_score = sum(scores) / n

print(f"Max:{max_score}")
print(f"Min:{min_score}")
print(f"Average:{round(average_score, 1)}")
print(f"Pass:{passing_count}")
