num = int(input())

binary_representation = ""
for i in range(7, -1, -1): 
    binary_representation += str((num >> i) & 1)  

print(binary_representation)  
