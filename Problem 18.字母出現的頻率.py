# 输入一行英文字串
input_string = input()

# 初始化字母计数列表，大小为 26，表示 A-Z
letter_count = [0] * 26

# 遍历输入字符串
for char in input_string:
    if char.isalpha():  # 检查是否为字母
        index = ord(char.upper()) - ord('A')  # 计算字母在列表中的索引
        letter_count[index] += 1  # 增加对应字母的计数

# 输出各字母出现的次数
output = ''
for count in letter_count:
    output += str(count) + ' '  # 拼接每个计数值

print(output.strip())  # 去掉最后的空格并打印
