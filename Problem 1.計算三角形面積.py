# 输入两个数字
x, y = input().split()  
base = int(x)  # 将第一个数字转换为整数
height = int(y)  # 将第二个数字转换为整数

# 计算三角形的面积
area = 0.5 * base * height  

# 输出面积，保留两位小数
print(f"Triangle area:{area:}")  # 使用 f-string 格式化输出
