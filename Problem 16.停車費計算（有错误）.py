time_start = input()
time_end = input()

# 解析开始时间和结束时间
s1 = int(time_start[:2])
s2 = int(time_start[3:5])
e1 = int(time_end[:2])
e2 = int(time_end[3:5])

# 计算停车时间的总分钟数
total_start_minutes = s1 * 60 + s2
total_end_minutes = e1 * 60 + e2

# 如果结束时间小于开始时间，说明跨天，按当天24小时计算
if total_end_minutes < total_start_minutes:
    total_end_minutes += 24 * 60  # 加上24小时（1440分钟）

duration_minutes = total_end_minutes - total_start_minutes

# 若停车时间小于30分钟，不计费
if duration_minutes < 30:
    total_fee = 0
else:
    # 计算停车时长的半小时数（向下取整）
    total_half_hours = duration_minutes // 30

    # 根据收费规则计算费用
    if total_half_hours <= 4:  # 前2小时（4个半小时内）
        total_fee = total_half_hours * 30
    elif total_half_hours <= 8:  # 超过2小时但不超过4小时（4到8个半小时之间）
        total_fee = (4 * 30) + ((total_half_hours - 4) * 40)
    else:  # 超过4小时
        total_fee = (4 * 30) + (4 * 40) + ((total_half_hours - 8) * 60)

print(total_fee)
