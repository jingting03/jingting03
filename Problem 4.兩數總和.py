# 输入测试用例的数量
n = int(input())

# 循环处理每个测试用例
for i in range(n):
    x, y = input().split()  # 输入两个数字
    first_integer = int(x)  # 将第一个数字转换为整数
    second_integer = int(y)  # 将第二个数字转换为整数

    # 输出两个整数的总和
    print(first_integer + second_integer)
