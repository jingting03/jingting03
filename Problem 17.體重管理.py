n = int(input())  # 输入有多少位会员要测量

# 遍历每位会员的BMI值
for _ in range(n):
    bmi = float(input())  # 输入每位会员的 BMI 值
    
    if bmi < 18.5:
        print("體重過輕")
    elif 18.5 <= bmi < 24:
        print("正常")
    elif 24 <= bmi < 28:
        print("體重過重")
    else:
        print("肥胖")
