n = int(input())

for _ in range(n):

    a, b = map(int, input().split())
    
    # 確保 a 小於 b，如果不是則交換
    if a > b:
        a, b = b, a
    
    # 創建一個空列表
    num_list = []
    
    # 使用 while 循環填充列表
    current = a
    while current <= b:
        num_list.append(current)
        current += 1
    
    # 計算總和並輸出結果
    total_sum = sum(num_list)
    print(total_sum)
