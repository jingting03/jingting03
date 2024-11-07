n = int(input())

arr = input().split()
for i in range(n):
    arr[i] = int(arr[i]) 

reversed_arr = arr[::-1]

result = ''
for num in reversed_arr:
    result += str(num) + ' ' 
print(result.strip())  
