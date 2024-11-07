# 定義數字的矩陣圖案
digit_map = {
    '0': ['*****', '*   *', '*   *', '*   *', '*****'],
    '1': ['    *', '    *', '    *', '    *', '    *'],
    '2': ['*****', '    *', '*****', '*    ', '*****'],
    '3': ['*****', '    *', '*****', '    *', '*****'],
    '4': ['*   *', '*   *', '*****', '    *', '    *'],
    '5': ['*****', '*    ', '*****', '    *', '*****'],
    '6': ['*****', '*    ', '*****', '*   *', '*****'],
    '7': ['*****', '    *', '    *', '    *', '    *'],
    '8': ['*****', '*   *', '*****', '*   *', '*****'],
    '9': ['*****', '*   *', '*****', '    *', '*****']
}

# 讀取輸入
num = input().strip()

# 輸出數字對應的矩陣圖案
for i in range(5):
    print(''.join(digit_map[digit][i] for digit in num))
