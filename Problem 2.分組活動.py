# 輸入人數n
n = int(input())

# 輸入號碼牌p
p = input()

# 輸入每組人數T
T = int(input())

# 用切片方式分組
groups = [p[i:i+T] for i in range(0, n, T)]

# 輸出分組結果
print(" ".join(groups))
