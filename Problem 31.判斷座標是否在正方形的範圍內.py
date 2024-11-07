a, b = input().split()

X = int(a)
Y = int(b)

if (X <= 100 and X >= 0) and (Y <= 100 and Y >= 0):
    print("inside")
else:
    print("outside")
