n = int(input())

for _ in range(n):
    num = int(input())
    temp_result = 1  
    for i in range(1, num + 1):  
        temp_result *= i  
    print(temp_result) 
