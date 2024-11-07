time_start = str(input())
time_end = str(input())

s1 = int(time_start[:2])
s2 = int(time_start[3:5])
e1 = int(time_end[:2])
e2 = int(time_end[3:5])

total_start_minutes = s1 * 60 + s2
total_end_minutes = e1 * 60 + e2

duration_minutes = total_end_minutes - total_start_minutes

if duration_minutes < 30:  
    total_fee = 0
else:
    total_half_hours = duration_minutes // 30
    if total_half_hours < 4: 
        if total_half_hours <= 2:
            total_fee = total_half_hours * 40
        else:
            total_fee = (2 * 40) + ((total_half_hours - 2) * 50)
    else:  
        total_fee = (4 * 40) + (4 * 50) + ((total_half_hours - 8) * 60)

print(int(total_fee))
