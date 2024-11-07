# 讀取輸入
input_value = input()

# 判斷數據類型
if input_value.isdigit():
    print("int")
elif input_value.replace('.', '', 1).isdigit() and input_value.count('.') == 1:
    print("float")
elif len(input_value) == 1:
    print("char")
else:
    print("string")
