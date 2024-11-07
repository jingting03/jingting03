a, b = input().split(',')
b = int(b)
stack = []

for digit in a:
    while b > 0 and stack and stack[-1] > digit:
        stack.pop()
        b -= 1
    stack.append(digit)

# 如果還有剩餘的 b 個數字需要刪除
result = ''.join(stack[:len(stack)-b])

# 移除結果前面的任何零並輸出最小值
print(int(result))  # 用 int 來自動移除前導零
