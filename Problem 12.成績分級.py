n = int(input())

for _ in range(n):
    score = int(input())

    if score >= 90:
        print("優等")
    elif score >= 80:
        print("甲等")
    elif score >= 70:
        print("乙等")
    elif score >= 60:
        print("丙等")
    else:
        print("不及格")
