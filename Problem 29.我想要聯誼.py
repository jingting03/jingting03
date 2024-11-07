# 讀取輸入
N = int(input())  # 女孩子的數量
girls_traits = input().split()  # 每位女孩子的特質，存儲為列表
K = input()  # 阿葉喜歡的特質，這是由數字組成的字符串

# 計數符合阿葉喜歡特質的女孩子數量
count = 0

for traits in girls_traits:
    # 將每個女孩子的特質拆成單個數字並檢查是否包含阿葉喜歡的特質
    if all(str(k) in traits for k in K):
        count += 1

# 輸出符合的女孩子數量
print(count)
