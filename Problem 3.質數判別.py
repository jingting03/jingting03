N = int(input())
if N <= 1:
    print("NO")  
else:
    is_prime = True 
    for i in range(2, N): 
        if N % i == 0: 
            is_prime = False 
            break 

    if is_prime:
        print("YES") 
    else:
        print("NO")  
