price_per_item = 100

P = int(input())

if P >= 100:
    total_price = P * price_per_item * 0.7  
elif P >= 30:
    total_price = P * price_per_item * 0.8 
elif P >= 10:
    total_price = P * price_per_item * 0.9  
else:
    total_price = P * price_per_item  

print(f"{total_price:.0f}")
