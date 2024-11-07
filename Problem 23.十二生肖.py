# 定義生肖對應字典
zodiac = {
    0: "rat",
    1: "ox",
    2: "tiger",
    3: "rabbit",
    4: "dragon",
    5: "snake",
    6: "horse",
    7: "sheep",
    8: "monkey",
    9: "rooster",
    10: "dog",
    11: "pig"
}

# 輸入四位數的西元年
year = int(input())

# 計算生肖
zodiac_index = (year - 4) % 12  # 4年是鼠年
zodiac_sign = zodiac[zodiac_index]  # 獲取生肖

# 輸出結果
print(zodiac_sign)
