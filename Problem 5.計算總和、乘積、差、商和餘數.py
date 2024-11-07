# 輸入兩個整數，中間用空白隔開
X, Y = input().split()
X = int(X)
Y = int(Y)

# 輸出四則運算的結果
print(f"{X}+{Y}={X + Y}")
print(f"{X}*{Y}={X * Y}")
print(f"{X}-{Y}={X - Y}")

# 計算商和餘數
quotient = X // Y
remainder = X % Y

# 如果餘數為負，則調整商和餘數
if remainder < 0:
    quotient += 1
    remainder -= Y

# 輸出商和餘數
print(f"{X}/{Y}={quotient}...{remainder}")
