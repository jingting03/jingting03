# 输入两个数字
x,y,z = input().split()  
upper_base = int(x)  # 将第一个数字转换为整数
lower_base = int(y)
height = int(z)  # 将第二个数字转换为整数

# 计算三角形的面积
area = (upper_base + lower_base) * height /2

# 输出面积，保留两位小数
print(f"Trapezoid area:{area:}")  # 使用 f-string 格式化输出
