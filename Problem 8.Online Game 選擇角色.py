# 建立一個字典來對應數字和輸出
output_map = {
    1: "Person",
    2: "Fairy"
}

# 讀取輸入的整數
n = int(input(""))  

# 根據輸入的數字輸出對應的文字
print(output_map.get(n, "Dwarf"))  # 如果n不在字典中，則輸出"Dwarf"
