c=int(input())

need_10=c//10
remaining=c%10

need_5=remaining//5
remaining=remaining%5

need_1=remaining

print(need_10)
print(need_5)
print(need_1)
