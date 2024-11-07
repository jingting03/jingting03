# 讀取正方形的數量
n = int(input())

# 逐行讀取每個邊長並計算面積
for _ in range(n):
    W = float(input())
    # 使用手動的四捨五入方法來達到你期望的輸出
    area = int(W * W * 10 + 0.5) / 10  # 將結果放大10倍再加上0.5，然後再縮小10倍
    print(area)
