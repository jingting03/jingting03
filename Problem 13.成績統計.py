# 輸入學生數量
x = int(input())

# 初始化總分變數
total_c = total_e = total_m = 0

# 讀入每個學生的成績並累加
for _ in range(x):
    c, e, m = map(int, input().split())
    total_c += c
    total_e += e
    total_m += m

# 計算各科和全班的平均成績
avg_c = total_c / x
avg_e = total_e / x
avg_m = total_m / x
avg_all = (total_c + total_e + total_m) / (x * 3)

# 輸出結果，四捨五入至小數點後1位
print(f"{avg_all:.1f} {avg_c:.1f} {avg_e:.1f} {avg_m:.1f}")
